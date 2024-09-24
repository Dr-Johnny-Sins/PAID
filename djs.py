import os,platform
os.system('git pull --quiet 2>/dev/null')
os.system("clear")
print('\033[97;1m [•] Join Whatsapp Group')
os.system('xdg-open https://chat.whatsapp.com/DWyyi8jb2w84cgp4MLhbAG')
djs=platform.architecture()[0]
if djs=="32bit":
    #__import__("p32")
    os.system("clear")
    exit('\033[91;1m [•] Sorry Bro 32 Bit Devices Not Supported')
elif djs=="64bit":
    __import__("p64")
