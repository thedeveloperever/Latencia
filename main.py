import pyfiglet
import os

import tweaks

def menu():
    print(pyfiglet.figlet_format("Latencia"))
    print("\t 1. Input Latency")
    print("\t 2. FPS")
    print("\t 3. Networking")
    print("\t 4. Exit")
    choice = int(input("Enter your choice [1, 2, 3, 4] :: "))
    os.system("cls")

    if choice == 1:
        tweaks.latency()
    if choice == 2:
        tweaks.fps()
    if choice == 3:
        tweaks.networking()
    if choice == 4:
        os._exit()
    if choice != 1 and != 2 and !=3 and !=4:
        print("\t Invalid Choice")

menu()
