#!/usr/bin/env python
# Author: br0k3ncode@github.com
# Date: 20241104
# Define the function name and take in any string entered into ip_address
def is_valid_ipv4(ip_address):
    # Splits ip address into octets at "."
    octets = ip_address.split('.')
    # Checks there are 4 octets
    if len(octets) != 4:
    # Iterates through the octets
    for octet in octets:
        # Check that each octet can be converted to an integer and
        # that is inclusivley between 0 and 255
        if (octet.isdigit() and 0 <= int(octet) <= 255):
            # If each octet is in parameters, script will continue.
            continue
    # If the ip_address does not meet all conditions above, the function returns False
        else:
            return False
    # If all conditions above are met, return True.
    return True

## Example usecase
def get_valid_ipv4_address():
    while True:
        device_ip = string(input("Enter an IPv4 address to program into your device: "))
        if is_valid_ipv4(device_ip) == True:
            print(f"{device_ip} is a valid address and is being programmed.")
            return device_ip
        else:
            print(f"The entry is not a proper IPv4 address, please try again.")

get_valid_ipv4_address()