#!/bin/bash
#udage ./ sequential_pinger.sh <subnet>
subnet=$1
timeout=1

#Extract base IP and range
IFS='/' read -r base range <<< "$subnet"
IFS='.' read -r o1 o2 o3 o4 <<< "$base"

#Loop through the last octet(1-254)
for i in {1..254}; do
    ip="$o1.$o2.$o3.$i"
    ping -c 1 -W $timeout "$ip" > /dev/null 2>&1

    if [ $? -eq 0 ]; then
        echo "[+] Host up: $ip"
    fi
done