#!/usr/local/bin/python3

import os
from can.interfaces.udp_multicast import UdpMulticastBus

VCAN_IP = os.getenv("VCAN_IP")

print(f"VCAN_IP: {VCAN_IP}")

if VCAN_IP is None:
    raise ValueError("VCAN_IP environment variable is not set")


with UdpMulticastBus(channel=VCAN_IP) as bus:
    try:
        for msg in bus:
            print(f"Received message: {msg}")
    except KeyboardInterrupt:
        pass
