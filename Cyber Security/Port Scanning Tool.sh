#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <IP_ADDRESS>"
    exit 1
fi

IP=$1

for port in {1..1024}; do

    nc -z -w 1 $IP $port 2>/dev/null
    if [ $? -eq 0 ]; then
        echo "Port $port is open"
    fi
done
