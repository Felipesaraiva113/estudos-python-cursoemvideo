import pyautogui
import time 
pyautogui.PAUSE=0.3
pyautogui.press('win')
pyautogui.write('bloco de notas')
pyautogui.press('enter')
time.sleep(5)
pyautogui.write('Estudar Python para ficar ainda melhor!')
pyautogui.hotkey('ctrl','s')
pyautogui.write('lembrete.txt')
pyautogui.press('enter')
time.sleep(2)
pyautogui.hotkey('alt','f4')
