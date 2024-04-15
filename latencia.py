# Latencia Optimizer
# Copyleft TheDeveloperEver

import pyfiglet
import os

inputtitle = pyfiglet.figlet_format("Input Latency")
fpstitle = pyfiglet.figlet_format("FPS")
nettitle = pyfiglet.figlet_format("Networking")

def titlescreen():
    title = pyfiglet.figlet_format("Latencia")
    print(title)
    print("\t 1. Input Latency")
    print("\t 2. FPS")
    print("\t 3. Networking")
    print("\t 4. General")
    titlechoice = int(input("Enter your choice [1, 2, 3, 4] :: "))
    os.system("cls")
    return titlechoice

choice = titlescreen()

if choice == 1:
    print(inputtitle)
    print("\t 1. Disable Extra Devices")
    print("\t 2. Change Win32PrioritySeparation")
    inputchoice = int(input("Enter your choice [1, 2] :: "))
    os.system("cls")

    if inputchoice == 1:
        print(inputtitle)
        os.system("sc config cdrom start=disabled")
        os.system("sc config cdfs start=disabled")
        os.system("sc config CompositeBus start=disabled")
        os.system("sc config umbus start=disabled")

    if inputchoice == 2:
        print(inputtitle)
        os.system("reg add 'HKLM\SYSTEM\CurrentControlSet\Control\PriorityControl' /v 'Win32PrioritySeparation' /t REG_DWORD /d 26 ")

if choice == 2:
    print(fpstitle)
    print("\t 1. Disable Extra Services")
    print("\t 2. Optimize Windows Settings")
    fpschoice = int(input("Enter your choice [1, 2] :: "))
    os.system("cls")

    if fpschoice == 1:
        print(fpstitle)
        os.system("sc config AxInstSV start=manual")
        os.system("sc config tzautoupdate start=manual")
        os.system("sc config dmwappushservice start=manual")
        os.system("sc config MapsBroker start=manual")
        os.system("sc config SharedAccess start=manual")
        os.system("sc config NetTcpPortSharing start=manual")
        os.system("sc config Spooler start=manual")
        os.system("sc config PrintNotify start=manual")
        os.system("sc config RmSvc start=manual")
        os.system("sc config RemoteAccess start=manual")
        os.system("sc config SCardSvr start=manual")
        os.system("sc config UserDataSvc start=manual")
        os.system("sc config WalletService start=manual")
        os.system("sc config WSearch start=manual")
        os.system("sc config DiagTrack start=manual")
        os.system("sc config RasMan start=manual")
        os.system("sc config SstpSvc start=manual")
        os.system("sc config DPS start=manual")
        os.system("sc config Spooler start=manual")
        os.system("sc config rdbss start=manual")
        os.system("sc config KSecPkg start=manual")
        os.system("sc config LanmanWorkstation start=manual")
        os.system("cls")

    if fpschoice == 2:
        print(fpstitle)
        os.system("powershell iwr 'https://raw.githubusercontent.com/thedeveloperever/Latencia/main/Resources/settings.reg' -o $Env:Temp\settings.reg")
        os.system("powershell reg import $Env:Temp\settings.reg")
        os.system("cls")

if choice == 3:
    print(nettitle)
    print("\t 1. Optimize NETSH Settings")
    print("\t 2. Optimize Ethernet Settings")
    print("\t 3. Optimize TCP Settings")
    netchoice = int(input("Enter your choice [1, 2] :: "))
    os.system("cls")

    if netchoice == 1:
        print(nettitle)
        os.system("netsh int tcp set global autotuninglevel=disabled")
        os.system("netsh int tcp set heuristics disabled disabled")
        os.system("netsh int tcp set supp congestionprovider=ctcp")
        os.system("cls")

    if netchoice == 2:
        print(nettitle)
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Flow Control' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Interrupt Moderation' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Large Send Offload v2 (IPv4)' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Large Send Offload v2 (IPv6)' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Priority & VLAN' -DisplayValue 'Priority & VLAN Enabled'")
        os.system("cls")

    if netchoice == 3:
        print(nettitle)
        os.system("powershell Set-NetTCPSetting -EcnCapability Enabled")
        os.system("powershell Set-NetTCPSetting -MaxSynRetransmissions 2")
        os.system("powershell Set-NetTCPSetting -MinRtoMs 300")
        os.system("powershell Set-NetTCPSetting -InitialRtoMs 2000")
        os.system("powershell Set-NetTCPSetting -Timestamps Enabled")
        os.system("cls")

titlescreen()
