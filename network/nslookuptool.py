import os

## Ping router - returns True or False
def ping_router(hostname):

    response = os.system("ping -c 1 " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def nslookup(hostname):

    response = os.system("nslookup " + hostname)

    #and then check the response...
    if response == 0:
        return True
    else:
        return False

def multilineinput():
    print("Please paste your multi-line input.\n"
          "To end, press ctrl+d on Linux/Mac, ctrl+z on Windows")
    lines = []
    try:
        while True:
            lines.append(input())
    except EOFError:
        pass
    return lines

def main():
    # switchlist = ["172.0.1.2", "sw-1", "sw-2", "8.8.8.8"]   # CUSTOMIZE THIS LIST WITH IPs to PING
    #inputlist()

    # Get input from User
    # inputlist should now be the variable the represents the list of servers being returned from multilineinput()
    inputlist= multilineinput()

    ## Use a loop to check each device for ICMP responses
    print("\n***** STARTING ICMP CHECKING *****")
    for x in inputlist:
        if ping_router(x):
            print(f"IP address {x} is responding to ICMP")
        else:
            print(f"IP address {x} is not responding to ICMP")

if __name__ == "__main__":
    main()
