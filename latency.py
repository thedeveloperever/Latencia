import pyfiglet
import os
import main

inputtitle = pyfiglet.figlet_format("Latency")
print("\t 1. Disable Extra Devices")
print("\t 2. Change Win32PrioritySeparation")
print("\t 3. Set Power Plan")
print("\t 4. Exit")
choice = int(input("Enter your choice [1, 2, 3, 4] :: "))
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
    print(inputtitle)
    os.system("powershell iwr 'https://raw.githubusercontent.com/thedeveloperever/Latencia/main/Resources/Latencia.pow' -o $Env:Temp\Latencia.pow")
    os.system("powershell powercfg /import $Env:Temp\Latencia.pow 44444444-4444-4444-4444-444444444444 ")

if choice == 4:
    main()
