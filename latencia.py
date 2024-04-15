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

titlescreen()

if titlechoice == 1:
    print(inputtitle)
    print("\t 1. Disable Extra Devices")
    print("\t 2. Disable USB Power Saving")
    print("\t 3. Change Win32PrioritySeparation")
    inputchoice = int(input("Enter your choice [1, 2] :: "))
    os.system("cls")

if titlechoice == 2:
    print(fpstitle)
    print("\t 1. Disable Extra Services")
    print("\t 2. Optimize Windows Settings")
    fpschoice = int(input("Enter your choice [1, 2] :: "))
    os.system("cls")

    if fpschoice == 1:
        print(fpstitle)
        os.system("powershell Set-Service AxInstSV -StartupType Disabled")
        os.system("powershell Set-Service tzautoupdate -StartupType Disabled")
        os.system("powershell Set-Service dmwappushservice -StartupType Disabled")
        os.system("powershell Set-Service MapsBroker -StartupType Disabled")
        os.system("powershell Set-Service SharedAccess -StartupType Disabled")
        os.system("powershell Set-Service NetTcpPortSharing -StartupType Disabled")
        os.system("powershell Set-Service Spooler -StartupType Disabled")
        os.system("powershell Set-Service PrintNotify -StartupType Disabled")
        os.system("powershell Set-Service RmSvc -StartupType Disabled")
        os.system("powershell Set-Service RemoteAccess -StartupType Disabled")
        os.system("powershell Set-Service SCardSvr -StartupType Disabled")
        os.system("powershell Set-Service UserDataSvc -StartupType Disabled")
        os.system("powershell Set-Service WalletService -StartupType Disabled")
        os.system("powershell Set-Service WSearch -StartupType Disabled")
        os.system("powershell Set-Service DiagTrack -StartupType Disabled")
        os.system("cls")

    titlescreen()    

    if fpschoice == 2:
        print(fpstitle)
        os.system("powershell iwr 'https://raw.githubusercontent.com/thedeveloperever/Latencia/main/Resources/settings.reg' -o $Env:Temp\settings.reg")
        os.system("powershell reg import $Env:Temp\settings.reg")
        os.system("cls")
    
    titlescreen()

if titlechoice == 3:
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

    titlescreen()
    
    if netchoice == 2:
        print(nettitle)
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Flow Control' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Interrupt Moderation' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Large Send Offload v2 (IPv4)' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Large Send Offload v2 (IPv6)' -DisplayValue 'Disabled'")
        os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Priority & VLAN' -DisplayValue 'Priority & VLAN Enabled'")
        os.system("cls")

    titlescreen()
    
    if netchoice == 3:
        print(nettitle)
        os.system("powershell Set-NetTCPSetting -EcnCapability Enabled")
        os.system("powershell Set-NetTCPSetting -MaxSynRetransmissions 2")
        os.system("powershell Set-NetTCPSetting -MinRtoMs 300")
        os.system("powershell Set-NetTCPSetting -InitialRtoMs 2000")
        os.system("powershell Set-NetTCPSetting -Timestamps Enabled")
        os.system("cls")
        
    titlescreen()
