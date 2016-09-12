#!/bin/bash

# add iptables rules to block docker from internet access

iptables -I FORWARD 1 -i docker0 -j DROP
iptables -I FORWARD 1 -i docker0 -d localhost -j ACCEPT
