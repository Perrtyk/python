import tkinter as tk
from tkinter import ttk, scrolledtext
from tkinter.font import Font
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
    output_console.insert(tk.END, msg + '\n')
    output_console.see(tk.END)


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
        hostname = socket.gethostbyaddr(ip_address)[0]
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Hostname is {hostname}\n')
        return hostname
    except socket.herror as e:
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Error resolving hostname: {e}\n')
        hostname = 'N/A'
        return hostname
    except Exception as e:
        print_debug(f'[{currentTime}] IP Scan ({ip_address}): Error: {e}\n')
        hostname = 'N/A'
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
        else:
            mac_address = get_mac_address(ip_address)

            ping_time = get_ping(ip_address)

            hostname = get_host_name(ip_address)

            progress_var.set(progress_var.get() + 1)

            print_debug(f"[{currentTime}] Processed IP Address: {ip_address} , Processed Ping: {ping_time}"
                        f" , Processed Hostname: {hostname}\n"
                        f"[{currentTime}] Processed MAC: {mac_address} ,"
                        f"Processed Connectivity: {available}\n")

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
root.columnconfigure(0, weight=1), root.columnconfigure(1, weight=2)
root.columnconfigure(3, weight=1), root.columnconfigure(3, weight=1)

# Create the input frame
input_frame = ttk.Frame(root, padding=(10, 10, 10, 30))
input_frame.grid(column=0, row=0, sticky='nsew')
input_frame.columnconfigure(0, weight=1, minsize=1)
input_frame.rowconfigure(0, weight=1, minsize=1)

# Create the start IP address label and entry
start_ip_label = ttk.Label(input_frame, text='Start IP Address:')
start_ip_label.grid(column=0, row=1, padx=(0, 10), sticky='we')
start_ip_entry = ttk.Entry(input_frame)
start_ip_entry.insert(0, '192.168.1.1')
start_ip_entry.grid(column=1, row=1, padx=(0, 20), sticky='we')

# Create the end IP address label and entry
end_ip_label = ttk.Label(input_frame, text='End IP Address:')
end_ip_label.grid(column=2, row=1, padx=(10, 0), sticky='we')
end_ip_entry = ttk.Entry(input_frame)
end_ip_entry.insert(0, '192.168.1.255')
end_ip_entry.grid(column=3, row=1, sticky='we')

# Create a custom style with a larger font size
button_style = ttk.Style()
button_style.configure('button_style.TButton', font=('Arial', 10), padding=1, sticky='nsew', pady=(0, 0), width=5,)

# Create the Scan button with a fixed width and the custom style
scan_button = ttk.Button(input_frame, text='Scan', style='button_style.TButton', command=lambda: threading.Thread(target=scan_ip_range, args=(start_ip_entry.get(), end_ip_entry.get(), progress_var)).start())
scan_button.grid(column=0, row=2, pady=(5, 0), sticky='we')

# Create the Stop Scan button
stop_scan_button = ttk.Button(input_frame, text='Stop Scan', command=stop_scan_func)
stop_scan_button.grid(column=3, row=2, pady=(5, 0), sticky='we')  # decreased pady value

# Create the results frame
results_frame = ttk.Frame(root, padding=(10, 0))
results_frame.grid(column=0, row=2, sticky='nsew')
root.rowconfigure(1, weight=1)
results_frame.columnconfigure(0, weight=1)

# Create the results treeview
results_columns = ('IP Address', 'Hostname', 'MAC Address', 'Ping', 'Connectivity')
results_treeview = ttk.Treeview(results_frame, columns=results_columns, show='headings')
results_treeview.grid(column=0, row=0, sticky='nsew')

# Configure the results treeview columns
for column in results_columns:
    results_treeview.heading(column, text=column)
    results_treeview.column(column, anchor='center')
    results_treeview.column(column, width=150)

# Create a scrollbar for the results treeview
results_scrollbar = ttk.Scrollbar(results_frame, orient='vertical', command=results_treeview.yview)
results_scrollbar.grid(column=1, row=0, sticky='ns')
results_treeview.configure(yscrollcommand=results_scrollbar.set)

# Create the progress bar
progress_var = tk.DoubleVar()
progress_bar = ttk.Progressbar(input_frame, variable=progress_var, maximum=100, value=0)
progress_bar.grid(column=0, row=3, columnspan=4, sticky='we')
percentage_label = ttk.Label(root, text='', anchor=tk.CENTER, font='TkDefaultFont 10 bold')
percentage_label.grid(row=6, column=0, columnspan=4, pady=5)

# Create the output console
console_font = Font(family='Consolas', size=8, weight='bold')
output_console = scrolledtext.ScrolledText(root, state='normal', height=11, font=console_font)
output_console.grid(column=0, row=2, sticky='nsew')

# Create the ping threshold label and drop down selector
ping_thresholds = [25, 50, 100, 250, 500]
selected_ping_threshold = tk.StringVar()
selected_ping_threshold.set(str(ping_thresholds[0]))
ping_threshold_label = ttk.Label(root, text='Ping Threshold (ms):')
ping_threshold_label.grid(column=0, row=4, padx=(0, 5), pady=(10, 0), sticky='nsew')
ping_threshold_selector = ttk.Combobox(root, textvariable=selected_ping_threshold, values=tuple(ping_thresholds), state="readonly")
ping_threshold_selector.grid(column=1, row=6, padx=(0, 5), pady=(10, 0), sticky='nsew')
ping_threshold_selector.columnconfigure(0, weight=5)


# Define a function to handle the selection change
def handle_ping_threshold_change(event):
    print_debug(f'[{currentTime}] Selected Ping Threshold: {selected_ping_threshold.get()}\n')

# Bind the selection change event to the function
ping_threshold_selector.bind("<<ComboboxSelected>>", handle_ping_threshold_change)

# Start the main loop
root.mainloop()