from importlib.resources import path
from pydoc import locate
from cv2 import repeat
import pyautogui
import random
import time
import os
import pygments
agents = [f"{path}/agents/brim.png", f"{path}/agents/breach.png", f"{path}/agents/cypher.png", f"{path}/agents/jett.png",
          f"{path}/agents/neon.png", f"{path}/agents/phoenix.png", f"{path}/agents/raze.png", f"{path}/agents/viper.png", f"{path}/agents/yoru.png",
          f"{path}/agents/chamber.png", f"{path}/agents/sage.png", f"{path}/agents/sova.png", f"{path}/agents/astra.png", f"{path}/agents/killjoy.png",
          f"{path}/agents/skye.png", f"{path}/agents/reyna.png"]
os.system("cls")
print("""
██╗   ██╗ █████╗ ██╗      ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██║   ██║██╔══██╗██║     ██╔═══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██║   ██║███████║██║     ██║   ██║██║     ██║   ██║██║     █████╔╝ 
╚██╗ ██╔╝██╔══██║██║     ██║   ██║██║     ██║   ██║██║     ██╔═██╗ 
 ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
made by Perchant76
tried only on 1920x1080
""")
print("path example: C:/Users/Perchant76/Documents/valorant auto lock")
path = input("insert path to this file> ")
print("""
[1] = Brimtone [10] = Viper [0] = RANDOM
[2] = Breach   [11] = Yoru 
[3] = Cypher   [12] = Chamber
[4] = Jett     [13] = Sage
[5] = Kayo     [14] = Sova
[6] = Neon     [15] = Astra
[7] = Omen     [16] = Killjoy
[8] = Phoenix  [17] = Skye
[9] = Raze     [18] = Reyna
""")
a = input("agent you want to instalock> ")
brim = (711, 927) and pyautogui.locateOnScreen(f"{path}/agents/brim.png")
braech = (627, 921) and pyautogui.locateOnScreen(f"{path}/agents/breach.png")
cyp = (873, 922) and pyautogui.locateOnScreen(f"{path}/agents/cypher.png")
jett = (968, 927) and pyautogui.locateOnScreen(f"{path}/agents/jett.png")
neon = (1131, 927) and pyautogui.locateOnScreen(f"{path}/agents/neon.png")
phoenix = (1299, 929) and pyautogui.locateOnScreen(
    f"{path}/agents/phoenix.png")
raze = (628, 1006) and pyautogui.locateOnScreen(f"{path}/agents/raze.png")
viper = (963, 1011) and pyautogui.locateOnScreen(f"{path}/agents/viper.png")
youru = (1040, 1014) and pyautogui.locateOnScreen(f"{path}/agents/yoru.png")
chamb = (789, 922) and pyautogui.locateOnScreen(f"{path}/agents/chamber.png")
sage = (794, 1005) and pyautogui.locateOnScreen(f"{path}/agents/sage.png")
sova = (871, 1004) and pyautogui.locateOnScreen(f"{path}/agents/sova.png")
astra = (1123, 1006) and pyautogui.locateOnScreen(f"{path}/agents/astra.png")
killjoy = (1211, 1007) and pyautogui.locateOnScreen(
    f"{path}/agents/killjoy.png")
skye = (1304, 1012) and pyautogui.locateOnScreen(f"{path}/agents/skye.png")
reyna = (710, 1023) and pyautogui.locateOnScreen(f"{path}/agents/reyna.png")
list = [brim, braech, cyp, jett, neon, phoenix, raze, viper,
        youru, chamb, sage, sova, astra, killjoy, skye, reyna]
if a == ("1"):
    print("start game...")
    while 1 < 5:
        time.sleep(0.1)
        if pyautogui.locateOnScreen(f"{path}/agents/brim.png"):
            z = pyautogui.doubleClick(711, 927)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("2"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/breach.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/breach.png"):
            b = pyautogui.doubleClick(627, 921)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)

elif a == ("3"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/cypher.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/cypher.png"):
            c = pyautogui.doubleClick(873, 922)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("4"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/jett.png"):
            repeat
        if pyautogui.locateOnScreen("/agents/jett.png"):
            d = pyautogui.doubleClick(968, 927)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("6"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/neon.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/neon.png"):
            e = pyautogui.doubleClick(1131, 927)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("7"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/phoenix.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/phoenix.png"):
            f = pyautogui.doubleClick(1299, 929)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("9"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/raze.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/raze.png"):
            g = pyautogui.doubleClick(628, 1006)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("10"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/viper.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/viper.png"):
            h = pyautogui.doubleClick(963, 1011)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("11"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/yoru.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/yoru.png"):
            i = pyautogui.doubleClick(1040, 1014)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("12"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/chamber.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/chamber.png"):
            j = pyautogui.doubleClick(789, 922)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("13"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/sage.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/sage.png"):
            k = pyautogui.doubleClick(794, 1005)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("14"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/sova.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/sova.png"):
            l = pyautogui.doubleClick(871, 1004)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("15"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/astra.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/astra.png"):
            m = pyautogui.doubleClick(1123, 1006)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("16"):
    print("start game...")
    while 1 < 2:
        time.sleep(0.1)
        if not pyautogui.locateOnScreen(f"{path}/agents/killjoy.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/killjoy.png"):
            n = pyautogui.doubleClick(1211, 1007)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("17"):
    print("start game...")
    while 1 < 2:
        if not pyautogui.locateOnScreen(f"{path}/agents/skye.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/skye.png"):
            o = pyautogui.doubleClick(1304, 1012)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("18"):
    print("start game...")
    while 1 < 2:
        if not pyautogui.locateOnScreen(f"{path}/agents/reyna.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/reyna.png"):
            p = pyautogui.doubleClick(710, 1023)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("0"):
    print("start game...")
    pyautogui.doubleClick(random.choice(list))
    pyautogui.moveTo(969, 812)
    pyautogui.click(969, 812)
else:
    print("invalid agent")
time.sleep(10)
