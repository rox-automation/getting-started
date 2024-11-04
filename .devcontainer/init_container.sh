#!/bin/bash

set -e

echo "Initializing container..."

pip install -r .devcontainer/requirements.txt

echo 'alias canview="python3 -m can.viewer -i udp_multicast -c $VCAN_IP"' >> /home/dev/.bashrc



# add container init code here
