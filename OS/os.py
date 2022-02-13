from OS.OSPrint import *

def showFetch(os, system):
    if os == "Windows" and system == "11":
        win11()
    elif os == "Windows" and (system == "10" or system =="8"):
        win10()
    elif os == "Windows" and system == "7":
        win7()
    elif os == "Linux":
        allLinux()
    elif os == "Darwin":
        apple()
    else:
        unknown()
