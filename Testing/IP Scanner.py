import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import ipaddress
import subprocess
import socket
from scapy.layers.l2 import ARP, Ether
from scapy.sendrecv import srp
from datetime import datetime

# Sets initial time and date
currentDateAndTime = datetime.now()
currentTime = currentDateAndTime.strftime("%d/%m/%Y %H:%M:%S")

# Prints debug command in both terminals
def print_debug(msg):
    global currentTime
    currentDateAndTime = datetime.now()
    currentTime = currentDateAndTime.strftime("%d/%m/%Y %H:%M:%S")
    print(msg)
    term.insert(tk.END, msg + '\n')
    term.see(tk.END)


def get_mac_address(ip_address):
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


# Define the function to check whether an IP address is available
def check_ip_address(ip_address):
    print_debug(f'[{currentTime}] Connect ({ip_address}): Running connection test . . .\n')
    response = subprocess.Popen(['ping', '-n', '1', '-w', '500', str(ip_address)],
                                stdout=subprocess.PIPE).communicate()[0]
    available, not_available = 'Yes', 'No'
    if b'Reply from' in response:
        if stop_scan:
            result = f'{not_available}'
            print_debug(f'[{currentTime}] Connect ({ip_address}): Complete, endpoint available: {result}.\n')
            return result
        else:
            result = f'{available}'
            print_debug(f'[{currentTime}] Connect ({ip_address}): Complete, endpoint available: {result}.\n')
            return result
    else:
        result = f'{not_available}'
        print_debug(f'[{currentTime}] Connect: Complete, endpoint available: {result}.\n')
        return result


# Define the function to scan a range of IP addresses and display the results in a table
def scan_ip_range(start_ip, end_ip, progress_var):
    # Initialize stop scan variable
    global stop_scan
    stop_scan = False
    # Clear the existing rows in the treeview
    print_debug(f'[{currentTime}] IP Scan: scan_ip_range . . .\n')
    for row in results_treeview.get_children():
        results_treeview.delete(row)
    print_debug(f'[{currentTime}] IP Scan: Clearing existing rows.\n')

    # Set the maximum value for the progress bar
    progress_var.set(int(ipaddress.ip_address(end_ip)) - int(ipaddress.ip_address(start_ip)) + 1)

    # Loop through the IP addresses in the range

    for i in range(int(ipaddress.ip_address(start_ip)), int(ipaddress.ip_address(end_ip))+1):
        if stop_scan:
            print_debug(f'[{currentTime}] Scan stopped.')
            break

        ip_address = str(ipaddress.ip_address(i))
        available = check_ip_address(ip_address)
        if available == 'No':
            print_debug(f'[{currentTime}] IP Scan ({ip_address}): Skipping, host is not available.\n')
            continue
        mac_address = get_mac_address(ip_address)
        ping_time = 'N/A'
        try:
            print_debug(f'[{currentTime}] IP Scan ({ip_address}): Gathering hostname . . .\n')
            hostname = socket.gethostbyaddr(ip_address)[0]

        except OSError:
            print_debug(f'[{currentTime}] IP Scan ({ip_address}): Hostname unavailable  (Operating System Error). . .\n')
            hostname = 'N/A'

        # Check if the IP address is available
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Checking Connectivity . . .\n')
        available = check_ip_address(ip_address)

        if available:
            # Try to get the MAC address (this can be slow)
            try:
                with (500):
                    print_debug(f'[{currentTime}] IP Scan ({ip_address}): Running MAC address process . . .\n')
                    mac_address = get_mac_address(ip_address)
            except:
                print_debug(f'[{currentTime}] IP Scan ({ip_address}): MAC process failed, OS Error.\n')
                pass

            # Try to get the hostname (this can also be slow)
            try:
                with (500):
                    print_debug(f'[{currentTime}] IP Scan ({ip_address}): Running hostname process . . .\n')
                    hostname = socket.gethostbyaddr(ip_address)[0]
            except:
                print_debug(f'[{currentTime}] IP Scan ({ip_address}): Hostname failed, OS Error.\n')
                pass

            # Try to ping the IP address
            try:
                print_debug(f'[{currentTime}] IP Scan ({ip_address}): Running PING process . . .\n')
                ping_response = subprocess.Popen(['ping', '-n', '4', '-w', '500', ip_address], stdout=subprocess.PIPE).communicate()[0]
                try:
                    if b'Reply from' in ping_response:
                        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Received ping response of {ping_response}.\n')
                        ping_time = str(ping_response).split("time=")[1].split("ms")[0] + ' ms'
                    else:
                        ping_time = 'Request timed out.'
                except:
                    pass
            except OSError:
                pass

        print_debug(f"[{currentTime}] Processed IP Address: {ip_address} , Processed Ping: {ping_time} , Processed Hostname: {hostname}\n"
              f"[{currentTime}] Processed MAC: {mac_address} , Processed Connectivity: {available}\n")

        # Add a row to the treeview with the IP address, hostname, MAC address, ping time, and availability
        results_treeview.insert('', 'end', values=(ip_address, hostname, mac_address, ping_time, available))

        # Increment the progress bar
        progress_var.set(progress_var.get() + 1)

    else:
        print_debug(f'[{currentTime}] Scan completed.')


# Define the function to stop the scan
def stop_scan_func():
    global stop_scan
    stop_scan = True


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
scan_button = ttk.Button(root, text='Scan', command=lambda: threading.Thread(target=scan_ip_range, args=(
start_ip_entry.get(), end_ip_entry.get(), progress_var)).start())
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
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(root, variable=progress_var, maximum=100)
progress_bar.pack(fill='x')

# create a scrolled text widget
term = scrolledtext.ScrolledText(root, height=12)
term.pack(side=tk.BOTTOM, fill=tk.X)

root.mainloop()