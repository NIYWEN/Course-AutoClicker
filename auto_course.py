# =====================================================================
# 免责声明 (Disclaimer):
# 本项目仅供 Python 自动化技术交流与学习使用。
# 请勿将此脚本用于任何违反学校/平台规定的商业或作弊行为。
# 使用者因滥用此代码产生的一切后果（包括但不限于封号、处分），
# 由使用者本人承担，开发者不承担任何连带责任。
# =====================================================================
import pyautogui
import time
import random
import pyperclip

# 读取文件
mesfile = open(r'D:\MyScripts\AutoClicker\urls.txt')
meslines = mesfile.readlines()
mesfile.close()
pyautogui.alert("读取文件完成。挂机程序启动，尽快切换到网课界面，退出将鼠标甩到左上角！")
time.sleep(5)
for url in meslines:
    time.sleep(1)
    clean = url.strip()
    pyperclip.copy(clean)

    pyautogui.hotkey('ctrl', 'l')
    time.sleep(0.5)

    pyautogui.hotkey('ctrl', 'v')
    time.sleep(0.5)

    pyautogui.press('enter')
    time.sleep(8)

    count = 0

    while count <= 100:
        time.sleep(5)

        try:
            loc_start = pyautogui.locateOnScreen('start.png', confidence=0.7)
        except:
            loc_start = None

        try:
            loc_submit = pyautogui.locateOnScreen('submit.png', confidence=0.7)
        except:
            loc_submit = None

        try:
            loc_start2 = pyautogui.locateOnScreen('start2.png', confidence=0.7)
        except:
            loc_start2 = None

        try:
            loc_end = pyautogui.locateOnScreen('end.png', confidence=0.7)
        except:
            loc_end = None

        if loc_start:
            b = random.randint(0, 5)
            pyautogui.click(1260 + b, 1078 + b, button='left')
            count += 1
            pyautogui.moveTo(99, 99)
            time.sleep(1)

        elif loc_submit:
            b = random.randint(0, 5)
            pyautogui.click(1178 + b, 1021 + b, button='left')
            count += 1
            pyautogui.moveTo(99, 99)
            time.sleep(1)

        elif loc_start2:
            b = random.randint(0, 5)
            pyautogui.click(1300 + b, 1031 + b, button='left')
            count += 1
            pyautogui.moveTo(99, 99)
            time.sleep(1)

        elif loc_end:
            b = random.randint(0, 5)
            #pyautogui.click(930 + b, 1014 + b, button='left')
            count += 1
            pyautogui.moveTo(99, 99)
            time.sleep(1)
            break