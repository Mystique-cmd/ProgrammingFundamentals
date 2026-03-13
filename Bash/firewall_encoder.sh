#!/bin/bash

parse_rule(){
    action="$1"
    proto="$2"
    from="$3"
    src="$4"
    to="$5"
    dest="$6"
    port_word="$7"
    port="$8"

    #Normalize keywords
    [[ "$src"=="any" ]] && src="0.0.0.0/0"
    [[ "$dest"=="any" ]] && dest="0.0.0.0/0"

    #Choose verdict
    [[ "$action"=="accept" ]] && verdict="ACCEPT"
    [[ "$action"=="drop" ]] && verdict="DROP"
    [[ "$action"=="reject" ]] && verdict="REJECT"

    echo "ip6tables -A INPUT -p $proto -s $src -d $dest --dport $port -j $verdict"
}

while IFS= read -r line; do
    parse_rule $line
done

# Use a rules.txt file to provide input