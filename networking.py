import pyfiglet
import os
import main

print(pyfiglet.figlet_format("Networking"))
print("\t 1. Optimize NETSH Settings")
print("\t 2. Optimize Ethernet Settings")
print("\t 3. Optimize TCP Settings")
print("\t 4. Exit")
choice = int(input("Enter your choice [1, 2, 3, 4] :: "))
os.system("cls")

if choice == 1:
    print(pyfiglet.figlet_format("Networking"))
    os.system("netsh int tcp set global autotuninglevel=disabled")
    os.system("netsh int tcp set heuristics disabled disabled")
    os.system("netsh int tcp set supp congestionprovider=ctcp")
    os.system("cls")

if choice == 2:
    print(pyfiglet.figlet_format("Networking"))
    os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Flow Control' -DisplayValue 'Disabled'")
    os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Interrupt Moderation' -DisplayValue 'Disabled'")
    os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Large Send Offload v2 (IPv4)' -DisplayValue 'Disabled'")
    os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Large Send Offload v2 (IPv6)' -DisplayValue 'Disabled'")
    os.system("powershell Set-NetAdapterAdvancedProperty -Name 'Ethernet' -DisplayName 'Priority & VLAN' -DisplayValue 'Priority & VLAN Enabled'")
    os.system("cls")

if choice == 3:
    print(pyfiglet.figlet_format("Networking"))
    os.system("powershell Set-NetTCPSetting -EcnCapability Enabled")
    os.system("powershell Set-NetTCPSetting -MaxSynRetransmissions 2")
    os.system("powershell Set-NetTCPSetting -MinRtoMs 300")
    os.system("powershell Set-NetTCPSetting -InitialRtoMs 2000")
    os.system("powershell Set-NetTCPSetting -Timestamps Enabled")
    os.system("cls")

if choice == 4:
    main()
