import subprocess
import threading
import re
import socket
from prettytable import PrettyTable
from blessed import Terminal
import time

def get_hostname(ip_address):
    try:
        return socket.gethostbyaddr(ip_address)[0]
    except socket.herror:
        return None

start_time = time.time()

def ping(ip_address, results):
    # send a ping command to the IP address
    # you can adjust the number of pings and timeout as needed
    process = subprocess.Popen(["ping", "-n", "1", "-w", "100", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    result = stdout.decode('utf-8') + stderr.decode('utf-8')

    # parse out the relevant data from the ping command output
    packet_loss = None
    average_latency = None

    match = re.search(r"(\d+)% packet loss", result)
    if match:
        packet_loss = int(match.group(1))

    match = re.search(r"Average = (\d+)ms", result)
    if match:
        average_latency = int(match.group(1))

    # get hostname and mac address using arp command
    arp_result = subprocess.Popen(["arp", "-a", ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    arp_output, arp_error = arp_result.communicate()
    arp_output = arp_output.decode('utf-8')

    hostname = get_hostname(ip_address)
    mac_address = None

    match = re.search(r"([0-9a-fA-F]{2}[:-]){5}([0-9a-fA-F]{2})", arp_output)
    if match:
        mac_address = match.group(0)

    # append a dictionary with the parsed results to the results list
    results.append({"ip_address": ip_address, "hostname": hostname, "mac_address": mac_address, "packet_loss": packet_loss, "average_latency": average_latency})

# create a list of IP addresses to ping
ip_addresses = [f"192.168.1.{i}" for i in range(1, 255)]

# create a list to store the ping results
results = []

# create a list of threads to execute the ping function for each IP address
threads = []
for ip in ip_addresses:
    print(f'Creating thread for {ip}')
    thread = threading.Thread(target=ping, args=(ip, results))
    threads.append(thread)
    thread.start()

# wait for all threads to finish
for thread in threads:
    print(f'Waiting for {thread} to finish.')
    thread.join()

# filter out IP addresses that did not respond to a ping
results = [r for r in results if r['average_latency'] is not None]

# sort the results by IP address
results = sorted(results, key=lambda x: [int(i) for i in x["ip_address"].split('.')])

# create a table from the results
table = PrettyTable(["IP Address", "Hostname", "MAC Address", "Packet Loss", "Avg Latency"])
for result in results:
    table.add_row([result["ip_address"], result["hostname"], result["mac_address"], f"{result['packet_loss']}%" if result["packet_loss"] is not None else "N/A", f"{result['average_latency']}ms"])

# print the table in the terminal
term = Terminal()
with term.fullscreen():
    duration = time.time() - start_time
    print(table)
    print(f"Scan completed in {duration:.2f} seconds")
    input()