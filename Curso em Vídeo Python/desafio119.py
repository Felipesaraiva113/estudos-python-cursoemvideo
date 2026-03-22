import pyautogui
import time 
pyautogui.PAUSE=0.3
pyautogui.press('win')
pyautogui.write('calculadora')
pyautogui.press('enter')
time.sleep(1)
pyautogui.press('7')
pyautogui.press('*')
pyautogui.press('8')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt','f4')
