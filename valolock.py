from cv2 import repeat
import pyautogui
import time
import os
os.system("cls")
print ("""
██╗   ██╗ █████╗ ██╗      ██████╗ ██╗      ██████╗  ██████╗██╗  ██╗
██║   ██║██╔══██╗██║     ██╔═══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝
██║   ██║███████║██║     ██║   ██║██║     ██║   ██║██║     █████╔╝ 
╚██╗ ██╔╝██╔══██║██║     ██║   ██║██║     ██║   ██║██║     ██╔═██╗ 
 ╚████╔╝ ██║  ██║███████╗╚██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗
  ╚═══╝  ╚═╝  ╚═╝╚══════╝ ╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝
made by Perchant76
works on 1920x1080
"be a dickhead atomaticly"
""")
print("path example: C:/Users/Perchant76/Documents/valorant auto lock")
path = input("insert path to this file> ")
print("""
[1] = Brimtone [10] = Viper
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
    print("start game...")
    while 1<5:
        if pyautogui.locateOnScreen(f"{path}/agents/brim.png"):
            pyautogui.doubleClick(711, 927)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a ==("2"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/breach.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/breach.png"):
            pyautogui.doubleClick(627, 921)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)

elif a == ("3"):
    print("start game...")
    while 1<2:
        
        if not pyautogui.locateOnScreen(f"{path}/agents/cypher.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/cypher.png"):
            pyautogui.doubleClick(873, 922)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("4"):
    print("start game...")
    while 1<2:
        
        if not pyautogui.locateOnScreen(f"{path}/agents/jett.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/jett.png"):
            pyautogui.doubleClick(968, 927)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("6"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/neon.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/neon.png"):
            pyautogui.doubleClick(1131, 927)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("7"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/phoenix.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/phoenix.png"):
            pyautogui.doubleClick(1299, 929)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("9"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/raze.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/raze.png"):
            pyautogui.doubleClick(628, 1006)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("10"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/viper.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/viper.png"):
            pyautogui.doubleClick(963, 1011)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("11"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/yoru.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/yoru.png"):
            pyautogui.doubleClick(1040, 1014)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("12"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/chamber.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/chamber.png"):
            pyautogui.doubleClick(789, 922)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("13"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/sage.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/sage.png"):
            pyautogui.doubleClick(794, 1005)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("14"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/sova.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/sova.png"):
            pyautogui.doubleClick(871, 1004)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("15"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/astra.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/astra.png"):
            pyautogui.doubleClick(1123, 1006)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("16"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/killjoy.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/killjoy.png"):
            pyautogui.doubleClick(1211, 1007)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("17"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/skye.png"):
            repeat
    if pyautogui.locateOnScreen(f"{path}/agents/skye.png"):
            pyautogui.doubleClick(1304, 1012)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)
elif a == ("18"):
    print("start game...")
    while 1<2:
        if not pyautogui.locateOnScreen(f"{path}/agents/reyna.png"):
            repeat
        if pyautogui.locateOnScreen(f"{path}/agents/reyna.png"):
            pyautogui.doubleClick(710, 1023)
            pyautogui.moveTo(969, 812)
            pyautogui.click(969, 812)

else:
    print ("invalid agent")