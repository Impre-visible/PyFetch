from uptime import uptime
import socket, platform, os, random, cpuinfo, GPUtil, psutil, subprocess
from screeninfo import get_monitors
from datetime import *
from platform import python_version
from time import *
from OS.os import *

def getScreen(screen, screenI):
    try:
        for m in get_monitors():
            screenI +=1
            screen += "Screen "+str(screenI)+" = "+ str(m.width) + "x" + str(m.height) +" "
        return screen
    except :
        return "Il n'y a pas d'écran dis donc"
screen0 = ""
screensI = 0

screens = getScreen(screen0, screensI)

def getCpuInfo():
    if platform.system() == "Windows":
        return cpuinfo.get_cpu_info()['brand_raw']
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        command = 'cat /proc/cpuinfo | grep "model name"'
        cpuInfo = subprocess.check_output(command, shell=True).strip().splitlines()[0]
        return cpuInfo[12:]
    return ""

def getGpuInfo():
    if platform.system() == "Windows":
        return gpuname()
    elif platform.system() == "Darwin":
        return subprocess.check_output(['/usr/sbin/sysctl', "-n", "machdep.cpu.brand_string"]).strip()
    elif platform.system() == "Linux":
        return "impossible d'accéder au GPU"
    return ""

usedMemory = round(psutil.virtual_memory()[3] * 0.000001)
allMemory = round(psutil.virtual_memory()[0] * 0.000001)
memory = f"{usedMemory}Mib / {allMemory}Mib"


allDiskList = []
usedDiskList = []
usedDisk = ""
allDisk = ""

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def gpuname():
    """Returns the model name of the first available GPU"""
    try:
        gpus = GPUtil.getGPUs()
    except:
        print("Unable to detect GPU model. Is your GPU configured? Are you running with nvidia-docker?")
        return "UNKNOWN"
    if len(gpus) == 0:
        raise ValueError("No GPUs detected in the system")
    return gpus[0].name 


def get_disk_info():
    disk_info = []
    for part in psutil.disk_partitions(all=False):
        if os.name == 'nt':
            if 'cdrom' in part.opts or part.fstype == '':
                # skip cd-rom drives with no disk in it; they may raise
                # ENOENT, pop-up a Windows GUI error for a non-ready
                # partition or just hang.
                continue
        usage = psutil.disk_usage(part.mountpoint)
        disk_info.append({
            'device':  part.device,
            'total':  usage.total,
            'used': usage.used,
            'used': usage.used,
            'percent': usage.percent,
            'fstype': part.fstype,
            'mountpoint': part.mountpoint
        })
    return disk_info 

def getAllStockage(listofdict):
    allDiskSpace = 0
    for item in listofdict:
        allDiskList.append(int(item["total"]))
    for val in allDiskList:
        allDiskSpace += val
    allDiskSpace/=1000000000
    return round(allDiskSpace,1)

def getusedStockage(listofdict):
    usedDiskSpace = 0
    for item in listofdict:
        usedDiskList.append(int(item["used"]))
    for val in usedDiskList:
        usedDiskSpace += val
    usedDiskSpace/=1000000000
    return round(usedDiskSpace,1)

now = datetime.now()
time = now.strftime("%H:%M:%S")
jour = date.today()
day = jour.strftime("%d/%m/%y")

CBlack = "\033[90m"
CRed = "\033[91m"
CGreen = "\033[92m"
CYellow = "\033[93m"
CYellow2 = "\033[33m"
CBlue = "\033[94m"
CPurple = "\033[95m"
CBeige = "\033[96m"
CWhite = "\033[97m"
CClear = "\033[30m"
CEnd = "\033[0m"

ColorList = [CRed, CGreen, CYellow, CYellow2, CBlue, CBeige]
color = random.choice(ColorList)
uname = platform.uname()
systemOS = platform.system()
system = platform.release()
username = os.getlogin()
hostname= socket.gethostname()
longueur = len(username + "@" + hostname)

UpTime = uptime()

d = UpTime // (24 * 3600)
UpTime = UpTime % (24 * 3600)
h = UpTime // 3600
UpTime %= 3600
m = UpTime // 60
UpTime %= 60
s = UpTime

def printAllDisk():
    try:
        allDisk = getAllStockage(get_disk_info())
        usedDisk = getusedStockage(get_disk_info())
        disk = f"{usedDisk} Go/{allDisk} Go used"
        return disk
    except PermissionError:
        return "impossible d'acceder aux infos des disques"

Uptime = f"{int(d)} days {int(h)} hours {int(m)} minutes {round(s)} seconds"

disk = printAllDisk()



cpu = getCpuInfo()
gpu = getGpuInfo()

pythonVersion = python_version()