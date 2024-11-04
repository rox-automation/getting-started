#!/usr/local/bin/python3

import os
import time
import can
from can.interfaces.udp_multicast import UdpMulticastBus

VCAN_IP = os.getenv("VCAN_IP")

if VCAN_IP is None:
    raise ValueError("VCAN_IP environment variable is not set")

# Create a bus instance
with UdpMulticastBus(channel=VCAN_IP) as bus:

    counter = 0

    try:
        while True:
            msg = can.Message(
                arbitration_id=0x123, data=[counter], is_extended_id=False
            )
            print(f"id: {msg.arbitration_id:#x} data: {msg.data.hex()}")
            bus.send(msg)
            time.sleep(1)
            counter += 1
            counter &= 0xFF

    except KeyboardInterrupt:
        pass
