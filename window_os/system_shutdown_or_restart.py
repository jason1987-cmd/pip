# System Shutdown or Restart

import os

def systemOffRestart():
    print("Enter r for Restart")
    print("Enter s for Shutdown")
    print("Enter any key for exit")

    option=input("Enter your option :")
    if option=='r':
        os.system('shutdown /r')
    elif option=='s':
        os.system('shutdown /s')
    else:
        exit()

    systemOffRestart()