import pyfiglet
import os
import main

print(pyfiglet.figlet_format("Latency"))
print("\t 1. Disable Extra Devices")
print("\t 2. Change Win32PrioritySeparation")
print("\t 3. Exit")
choice = int(input("Enter your choice [1, 2, 3] :: "))
os.system("cls")

if choice == 1:
    print(inputtitle)
    os.system("sc config cdrom start=disabled")
    os.system("sc config cdfs start=disabled")
    os.system("sc config CompositeBus start=disabled")
    os.system("sc config umbus start=disabled")
    os.system("cls")

if choice == 2:
    print(inputtitle)
    os.system("reg add HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl /v Win32PrioritySeparation /t REG_DWORD /d 26")
    os.system("cls")

if choice == 3:
    main()
