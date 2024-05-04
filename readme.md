# Snapchat Discovery Story Blocker
This repository contains a script that writes a few rules into the `FORWARD` chain of `iptables`. These rules block a few content servers that Snapchat uses to serve normal and discovery stories. 

This is intended to work with OpenVPN servers running in a Linux Environment.

Basically, this script blocks Snapchat stories including Normal User Stories and Discovery Stories. It does not block messaging or any other Snapchat feature. 

> **Note:** This script is intended to be used with OpenVPN servers running in a Linux environment. It will not work with other VPN servers or on Windows.
> There are many videos on how to make your own VPN using cheap VPS servers and OpenVPN. I recommend you watch one of those videos if you are new to VPNs.

## Why?
It's just a productivity hack that I've been sitting on for a year now. I've been wanting to create a VPN server that blocks out Snapchat stories (which is my greatest vice right now).

You might say: 
> Just Delete Snapchat. 

A lot of us can't, mainly due to the fact that many of our relationships are maintained using Snapchat.

## Prerequisites

### OpenVPN
Please have `openvpn-server` installed on your machine. There is an easy-to-use script [here](https://github.com/angristan/openvpn-install). After setting up and ensuring that devices can connect to your server, you may proceed with the setup.

### Python
Just have `python` installed on your machine; it's pretty simple. There are many tutorials online on how to install Python onto your machine.

## Installation 
Just clone this repository and execute `iptables.py` as root (or using sudo) 
`sudo python3 iptables.py`

It will clear your `FORWARD` table and insert `REJECT` rules for IPs based on the `detected.ip.txt` file.

### Startup

The script will output some text describing what it is, but also some debug stuff such as the IPs detected and a Wireshark predicate that will come in handy for sniffing IPs on a VPN.

## "It Doesn't Work"
This script may not work for everyone due to the fact that many different content servers exist to serve different regions in the world.

### Blocking more Snapchat Server's
To fix this issue and block Snapchat for your server's region, you may need to use Wireshark and sniff out IP addresses that correlate with watching a story. This isn't hard but I recommend setting up a virtual machine running *Ubuntu 22.04* and using Wireshark in sudo mode to sniff the `tun0` adapter.

Write down the IPs that you think are responsible for serving stories. Once you are sure, you can append them to the `detected.ip.txt` file and then rerun the script.

However, be careful with what IPs you block because you may accidentally block Snapchat's messaging server. If you make this mistake, simply remove the incorrect IP from `detected.ip.txt` and rerun the script.

## Contributions

Any improvements to the script are welcome however any successful additions to the `detected.ip.txt` file should be pulled into the repository so we can all have a better no-story Snapchat experience.
