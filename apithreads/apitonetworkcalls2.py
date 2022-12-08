#!/usr/bin/python3
"""API requests with threads | rzfeeser@alta3.com"""

from concurrent.futures import ThreadPoolExecutor, as_completed
from time import time
from netmiko import ConnectHandler

arista1 = {
    'device_type': 'arista_eos',
    'host':   'sw-1',
    'username': 'admin',
    'password': 'alta3',
    }

arista2 = {
    'device_type': 'arista_eos',
    'host':   'sw-2',
    'username': 'admin',
    'password': 'alta3',
    }

all_devices = [arista1, arista2]

def netcommand(**a_device):
    net_connect = ConnectHandler(**a_device)
    output = net_connect.send_command("show arp")
    print(f"\n\n--------- Device {a_device['device_type']} ---------")
    print(output)
    print("--------- End ---------")

start = time()

processes = []

with ThreadPoolExecutor(max_workers=5) as executor:
    for device in all_devices:
        processes.append(executor.submit(netcommand, **device))   # add a new task to the threadpool and store in processes list

for task in as_completed(processes):    # yields the items in processes as they complete (it finished or was canceled)
    print(task.result())

# display the total run time
print(f'Time taken: {time() - start}')
