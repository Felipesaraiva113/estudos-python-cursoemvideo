import pyautogui
import time
pyautogui.PAUSE=0.3
pyautogui.press('win')
pyautogui.write('firefox')
pyautogui.press('enter')
time.sleep(1)
pyautogui.write('canva')
pyautogui.press('enter')
time.sleep(3)
pyautogui.click(x=196, y=693)
time.sleep(3)
pyautogui.click()
for i in range(1,17):
    time.sleep(3)
    pyautogui.press('right')
    