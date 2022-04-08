from importlib.resources import path
from pydoc import locate
from cv2 import repeat
import pyautogui
import random
import time
import os
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
if a == ("1"):
    def z():
        print("start game...")
        while 1 < 5:
            time.sleep(0.1)
            if pyautogui.locateOnScreen(f"{path}/agents/brim.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("2"):
    def b():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/breach.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/breach.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)

elif a == ("3"):
    def c():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/cypher.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/cypher.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("4"):
    def d():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/jett.png"):
                repeat
            if pyautogui.locateOnScreen("/agents/jett.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("6"):
    def e():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/neon.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/neon.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("7"):
    def f():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/phoenix.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/phoenix.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("9"):
    def g():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/raze.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/raze.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("10"):
    def h():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/viper.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/viper.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("11"):
    def i():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/yoru.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/yoru.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("12"):
    def j():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/chamber.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/chamber.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("13"):
    def k():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/sage.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/sage.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("14"):
    def l():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/sova.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/sova.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("15"):
    def m():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/astra.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/astra.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("16"):
    def n():
        print("start game...")
        while 1 < 2:
            time.sleep(0.1)
            if not pyautogui.locateOnScreen(f"{path}/agents/killjoy.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/killjoy.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("17"):
    def o():
        print("start game...")
        while 1 < 2:
            if not pyautogui.locateOnScreen(f"{path}/agents/skye.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/skye.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("18"):
    def p():
        print("start game...")
        while 1 < 2:
            if not pyautogui.locateOnScreen(f"{path}/agents/reyna.png"):
                repeat
            if pyautogui.locateOnScreen(f"{path}/agents/reyna.png"):
                pyautogui.doubleClick(711, 927)
                pyautogui.moveTo(969, 812)
                pyautogui.click(969, 812)
elif a == ("0"):
    xy = random.choice(agents)
    if not pyautogui.locateAllOnScreen(xy):
        repeat
    if pyautogui.locateAllOnScreen(xy):
        pyautogui.doubleClick(xy)
        pyautogui.moveTo(969, 812)
        pyautogui.click(969, 812)

else:
    print("invalid agent")
