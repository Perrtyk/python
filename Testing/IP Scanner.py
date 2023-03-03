import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import ipaddress
import subprocess
import socket
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from datetime import datetime


# Global Variables
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%d/%m/%Y %H:%M:%S")
scan_in_progress = False
stop_scan = False
socket.setdefaulttimeout(0.350)


# Prints debug command in both terminals. Updates the currentTime variable to reflect most recent time.
def print_debug(msg):
    global currentTime
    currentTime = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(msg)
    term.insert(tk.END, msg + '\n')
    term.see(tk.END)


def get_ping(ip_address):
    if stop_scan:
        ping_time = 'N/A'
        return ping_time
    print_debug(f'[{currentTime}] IP Scan ({ip_address}): Running PING process . . .\n')
    ping_response = subprocess.Popen(['ping', '-n', '3', '-w', '350', ip_address],
                                         stdout=subprocess.PIPE).communicate()[0]
    if b'Reply from' in ping_response:
        ping_time = str(ping_response).split("Average =")[1].split("ms")[0] + ' ms'
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Received ping response of{ping_time}.\n')
        return ping_time
    else:
        ping_time = 'Request timed out.'
        return ping_time


# Define the function to check whether an IP address is available
def check_ip_address(ip_address):
    message_connect = f'[{currentTime}] Connect ({ip_address}):'
    print_debug(f'{message_connect} Running connection test . . .\n')
    response = subprocess.Popen(['ping', '-n', '1', '-w', '350', str(ip_address)],
                                stdout=subprocess.PIPE).communicate()[0]
    available, not_available = 'Yes', 'No'
    if b'Reply from' in response:
        if stop_scan:
            result = f'{not_available}'
            print_debug(f'{message_connect} Complete, endpoint available: {result}.\n')
            return result
        else:
            result = f'{available}'
            print_debug(f'{message_connect} Complete, endpoint available: {result}.\n')
            return result
    else:
        result = f'{not_available}'
        print_debug(f'{message_connect} Complete, endpoint available: {result}.\n')
        return result


def get_mac_address(ip_address):
    print_debug(f'[{currentTime}] IP Scan ({ip_address}): Running MAC address process . . .\n')
    message_mac = f'[{currentTime}]     MAC ({ip_address}):'
    if stop_scan:
        mac_address = 'N/A'
        return mac_address
    elif not stop_scan:
        # Create an ARP request packet for the given IP address
        print_debug(f'{message_mac} Attempting to gather MAC address via ARP . . .\n')
        arp_request = ARP(pdst=ip_address)

        # Create an Ethernet frame with the broadcast destination MAC address
        ether = Ether(dst='ff:ff:ff:ff:ff:ff')

        # Combine the ARP request packet and Ethernet frame
        packet = ether / arp_request

        try:
            # Send the packet and receive the response
            print_debug(f'{message_mac} Sending out packet and awaiting response . . .\n')
            result = srp(packet, timeout=3, verbose=0)[0]

            # Extract the MAC address from the response
            mac_address = result[0][1].hwsrc
            print_debug(f'{message_mac} Extracting MAC from response . . .\n')
        except IndexError:
            # Return 'N/A' if an index error occurs
            print_debug(f'{message_mac} Index error, return N/A . . .\n')
            mac_address = 'N/A'
        print_debug(f'{message_mac} Returned MAC address . . .\n')
        return mac_address
    else:
        mac_address = 'N/A'
        print_debug(f'{message_mac} Endpoint unavailable . . .\n')
        return mac_address


def get_host_name(ip_address):
    print_debug(f'[{currentTime}] IP Scan ({ip_address}): Gathering hostname . . .\n')
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(0.2)
            s.connect((ip_address, 80))
            hostname = socket.gethostbyaddr(ip_address)[0]
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Hostname is {hostname}\n')
    except (socket.gaierror, socket.timeout, ConnectionRefusedError):
        hostname = '.N/A'
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Hostname lookup failed\n')
    return hostname

# Define the function to scan a range of IP addresses and display the results in a table
def scan_ip_range(start_ip, end_ip, progress_var):
    # Initialize stop scan variable
    global stop_scan, scan_in_progress
    stop_scan = False
    scan_in_progress = True
    disable_scan_button()
    # Clear the existing rows in the treeview
    print_debug(f'[{currentTime}] IP Scan: scan_ip_range . . .\n')
    for row in results_treeview.get_children():
        results_treeview.delete(row)
    print_debug(f'[{currentTime}] IP Scan: Clearing existing rows.\n')

    # Set the maximum value for the progress bar
    progress_var.set(0)
    max_val = int(ipaddress.ip_address(end_ip)) - int(ipaddress.ip_address(start_ip))
    if max_val == 0:
        max_val = 1
    progress_bar["maximum"] = max_val

    # Loop through the IP addresses in the range

    for i in range(int(ipaddress.ip_address(start_ip)), int(ipaddress.ip_address(end_ip))+1):
        if stop_scan:
            print_debug(f'[{currentTime}] Scan stopped.')
            break

        ip_address = str(ipaddress.ip_address(i))
        percentage = int((i - int(ipaddress.ip_address(start_ip))) * 100 / max_val)
        percentage_label.config(text=f'{percentage}% | Scanning: {ip_address}')
        available = check_ip_address(ip_address)
        if available == 'No':
            print_debug(f'[{currentTime}] IP Scan ({ip_address}): Skipping, host is not available.\n')
            progress_var.set(progress_var.get() + 1)
            continue

        mac_address = get_mac_address(ip_address)

        ping_time = get_ping(ip_address)

        hostname = get_host_name(ip_address)

        progress_var.set(progress_var.get() + 1)

        print_debug(f"[{currentTime}] Processed IP Address: {ip_address} , Processed Ping: {ping_time} , Processed Hostname: {hostname}\n"
                    f"[{currentTime}] Processed MAC: {mac_address} , Processed Connectivity: {available}\n")

        # Add a row to the treeview with the IP address, hostname, MAC address, ping time, and availability
        results_treeview.insert('', 'end', values=(ip_address, hostname, mac_address, ping_time, available))

    else:
        print_debug(f'[{currentTime}] Scan completed.')
        scan_in_progress = False
        enable_scan_button()


# Define the function to stop the scan
def stop_scan_func():
    global stop_scan, scan_button
    scan_button.config(state="normal", text="Scan")
    stop_scan = True


def disable_scan_button():
    global scan_in_progress, scan_button
    scan_in_progress = True
    scan_button.config(state="disabled", text="Scanning...")

def enable_scan_button():
    global scan_in_progress, scan_button
    scan_in_progress = False
    scan_button.config(state="normal", text="Scan")

# Create the main window
root = tk.Tk()
root.title('IP Scanner')

# Create the input frame
input_frame = ttk.Frame(root, padding=(10, 10, 10, 0))
input_frame.pack(fill='x')

# Create the start IP address label and entry
start_ip_label = ttk.Label(input_frame, text='Start IP Address:')
start_ip_label.pack(side='left', padx=(0, 10))
start_ip_entry = ttk.Entry(input_frame)
start_ip_entry.insert(0, '192.168.1.1')
start_ip_entry.pack(side='left', fill='x', expand=True)

# Create the end IP address label and entry
end_ip_label = ttk.Label(input_frame, text='End IP Address:')
end_ip_label.pack(side='left', padx=(10, 10))
end_ip_entry = ttk.Entry(input_frame)
end_ip_entry.insert(0, '192.168.1.255')
end_ip_entry.pack(side='left', fill='x', expand=True)

# Create the Scan button
scan_button = ttk.Button(root, text='Scan', command=lambda: threading.Thread(target=scan_ip_range, args=(start_ip_entry.get(), end_ip_entry.get(), progress_var)).start())
scan_button.pack(pady=(10, 0))

# Create the Stop Scan button
stop_scan_button = ttk.Button(input_frame, text='Stop Scan', command=stop_scan_func)
stop_scan_button.pack(side='left', pady=(10, 0))

# Create the results frame
results_frame = ttk.Frame(root, padding=(10, 0))
results_frame.pack(fill='both', expand=True)

# Create the results treeview
results_columns = ('IP Address', 'Hostname', 'MAC Address', 'Ping Time', 'Available')
results_treeview = ttk.Treeview(results_frame, columns=results_columns, show='headings')
for column in results_columns:
    results_treeview.heading(column, text=column)
    results_treeview.column(column, width=150)

# Create the scrollbar for the results treeview
results_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=results_treeview.yview)

# Attach the scrollbar to the treeview
results_treeview.config(yscrollcommand=results_scrollbar.set)
results_scrollbar.pack(side='right', fill='y')
results_treeview.pack(fill='both', expand=True)

# Create the progress bar
progress_var = tk.IntVar()
progress_var.set(0)
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill=tk.X, padx=10, pady=10)

percentage_label = ttk.Label(root, text='0%')
percentage_label.pack(pady=10)

# create a scrolled text widget
term = scrolledtext.ScrolledText(root, height=12)
term.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()

#get_host_name('192.168.1.1')
