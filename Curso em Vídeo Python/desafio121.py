import pyautogui
import time
def enter():
    pyautogui.press('enter')
def abas(a):
    pyautogui.write(a)
    enter()
    time.sleep(7)
def abas2():
    pyautogui.hotkey('ctrl','t')
pyautogui.PAUSE=0.3
pyautogui.press('win')
pyautogui.write('firefox')
enter()
time.sleep(1)
abas('https://classroom.google.com/u/1/h')
abas2()
abas('https://edu.delightex.com/Studio/Class/6xkys/Assignments')
abas2()
abas('https://framevr.io/murilo2100#hall-1')
time.sleep(10)
pyautogui.hotkey('alt','f4')
