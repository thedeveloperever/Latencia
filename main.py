import pyfiglet
import os

import latency.py
import fps.py
import networking.py

title = pyfiglet.figlet_format("Latencia")

print(title)
print("\t 1. Input Latency")
print("\t 2. FPS")
print("\t 3. Networking")
choice = int(input("Enter your choice [1, 2, 3] :: "))
os.system("cls")

if choice == 1:
    latency()
if choice == 2:
    fps()
if choice == 3:
    networking()
