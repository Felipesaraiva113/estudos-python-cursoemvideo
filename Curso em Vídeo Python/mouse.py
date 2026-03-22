import pyautogui
import time
 
# Espera 5 segundos antes de mostrar a posição do mouse
time.sleep(5)
 
# Obtém a posição do ponteiro do mouse
x, y = pyautogui.position()
 
# Imprime a posição
print(f'A posição atual do ponteiro é: X={x}, Y={y}')
