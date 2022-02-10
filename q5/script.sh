#!/bin/bash

set -eux 

get_port () {
    PID=$1
    sudo netstat -lntup | grep ${PID} | awk {'print $4'}
}

echo getting process details
top -b -n1 -o%MEM | head -n10 | tail -n4 | tail -n1 | awk {'printf ("%s\n%s\n%s\n%s", $12, $9, $10, $1)'} > out.txt

echo getting port
get_port $(cat out.txt | tail -n1) >> out.txt
