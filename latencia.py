# Latencia Optimizer
# Copyleft TheDeveloperEver

import pyfiglet
import os

inputtitle = pyfiglet.figlet_format("Input Latency")
fpstitle = pyfiglet.figlet_format("FPS")
nettitle = pyfiglet.figlet_format("Networking")


title = pyfiglet.figlet_format("Latencia")
print(title)

print("\t 1. Input Latency")
print("\t 2. FPS")
print("\t 3. Networking")

titlechoice = input("Enter your choice [1, 2, 3] :: ")

if titlechoice == 1:
    print(inputtitle)
    print("\t 1. Disable Extra Devices")
    print("\t 2. Disable Mouse Acceleration")
    print("\t 3. Change Win32PrioritySeparation")
    inputchoice = input("Enter your choice [1, 2, 3] :: ")

if titlechoice == 2:
    print(fpstitle)
    print("\t 1. Disable Extra Services")
    print("\t 2. Optimize Windows Settings")
    print("\t 3. Disable Defender")
    fpschoice = input("Enter your choice [1, 2, 3] :: ")

if titlechoice == 3:
    print(nettitle)
    print("\t 1. Optimize Ethernet Adapter")
    print("\t 2. Optimize WiFi Adapter")
    print("\t 3. Optimize NETSH Settings")
    netchoice = input("Enter your choice [1, 2, 3] :: ")
