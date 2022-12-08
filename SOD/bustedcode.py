#!/usr/bin/env python3

import time
import sys
import os
import paramiko
import netifaces

def delay_print(s):
    # there's nothing wrong with this function, it's just some cool code that
    # will print out strings one character at a time! :)
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)

def main():
    delay_print("Good morning, Mr. Stark. Here are your network interfaces:\n")
    print(netifaces.interfaces())
    
    try:
        for i in netifaces.interfaces():
            # with open("challenge.log") as foo:                 # opens writeable file for logging
            print('Logging addresses for interface ' + i)     # prints name of interface being logged
            print('MAC: ', end='')
            print((netifaces.ifaddresses(i)[netifaces.AF_LINK])[0]['addr']) #, file=bar) # Prints the MAC address to file
            print('IP: ', end='')
            print((netifaces.ifaddresses(i)[netifaces.AF_INET])[0]['addr']) #, file=bar) # Prints the IP address to file
    except:
        print('Could not collect adapter information') # Print an error message

main()
