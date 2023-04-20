from concurrent.futures import ThreadPoolExecutor
from PigeonTool import PigeonTool
import time
import psutil

tool = PigeonTool()
ips = [f"192.168.1.{i}" for i in range(1, 255)]
start_time = time.time()

def scan(ip):
    # Execute the three functions in sequence for the given IP address
    start_time = time.time()
    alive = tool.connect(ip)
    duration_alive = time.time() - start_time

    if alive == 'Yes':
        start_time = time.time()
        ping = tool.ping(ip)
        duration_ping = time.time() - start_time

        start_time = time.time()
        host = tool.hostname(ip)
        duration_host = time.time() - start_time

        start_time = time.time()
        mac = tool.mac_address(ip)
        duration_mac = time.time() - start_time

        print(f'time {duration_alive}{alive}\ntime {duration_ping}{ping}\n'
          f'time {duration_host}{host}\ntime {duration_mac}{mac}')

# Determine the optimal number of threads based on CPU usage
cpu_count = psutil.cpu_count(logical=False)
print(f'CPU Count: {cpu_count}')
cpu_percent = psutil.cpu_percent(interval=1)
print(f'CPU %: {cpu_percent}')

# Determine the number of threads to use based on CPU usage and number of IPs to scan
num_threads = min(len(ips), max(1, int(cpu_count * (1 - cpu_percent/100))))
print(f'Thread Numbers: {num_threads}')

# Create a thread pool with the determined number of threads
with ThreadPoolExecutor(max_workers=num_threads) as executor:
    # Submit each IP address to the thread pool for scanning
    for ip in ips:
        executor.submit(scan, ip)

duration_total = time.time() - start_time
print(duration_total)
