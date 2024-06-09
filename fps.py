import pyfiglet
import os
import main

print(pyfiglet.figlet_format("FPS"))
print("\t 1. Disable Extra Services")
print("\t 2. Optimize Windows Settings")
print("\t 3. Disable Defender")
print("\t 4. Exit")
choice = int(input("Enter your choice [1, 2, 3, 4] :: "))
os.system("cls")


if choice == 1:
    print(pyfiglet.figlet_format("FPS"))
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

if choice == 2:
    print(pyfiglet.figlet_format("FPS"))
    os.system("powershell iwr 'https://raw.githubusercontent.com/thedeveloperever/Latencia/main/Resources/settings.reg' -o $Env:Temp\settings.reg")
    os.system("powershell reg import $Env:Temp\settings.reg")
    os.system("cls")

if choice == 3:
    print(pyfiglet.figlet_format("FPS"))
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableAntiSpyware /t REG_DWORD /d 1')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v DisableRoutinelyTakingAction /t REG_DWORD /d 1')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender" /v ServiceKeepAlive /t REG_DWORD /d 0')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableBehaviorMonitoring /t REG_DWORD /d 1')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableIOAVProtection /t REG_DWORD /d 1')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableOnAccessProtection     /t REG_DWORD /d 1')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Real-Time Protection" /v DisableRealtimeMonitoring /t REG_DWORD /d 1')
    os.system('reg add "HKLM\SOFTWARE\Policies\Microsoft\Windows Defender\Reporting" /v DisableEnhancedNotifications /t REG_DWORD /d 1')
    os.system("cls")

if choice == 4:
    main()
