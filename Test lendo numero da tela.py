from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)

import pyautogui
import pygetwindow
import gc
import time
import pytesseract
from playsound import playsound
import keyboard
import pydirectinput
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #necessario para funcionar

# mana = pyautogui.screenshot('mana.png', region=(2070,220, 40, 15))
# mana_atual = pytesseract.image_to_string(mana, config='--psm 3, -c tessedit_char_whitelist=0123456789')
# print(mana_atual)
# mana.show()

# mana = pyautogui.screenshot('mana.png')
# mana_atual = pytesseract.image_to_string(mana, config='--psm 6, tessedit_char_whitelist=0123456789')
# print(mana_atual)
# mana.show()


# mana_int = int(mana_atual) # converte a string para int para ser usada como condicao
# # print(mana_int)
# time.sleep(3)

# while(True):
#     if mana_int >= 111:
#         pyautogui.click(x=3829, y=101)
#         keyboard.press_and_release('f11')
#         break
#     if keyboard.is_pressed('esc'):
#         print("saindo")
#         break;
# #         print("mana baixa")

""" Test loop apenas printando bugando no numero 74"""
while(True):
    mana = pyautogui.screenshot('mana.png', region=(2070,220, 40, 15))
    mana_atual = pytesseract.image_to_string(mana, config='--psm 6, tessedit_char_whitelist=0123456789')
    print(mana_atual)

#     hotkey = 'ctrl+f3'
#     keyboard.add_hotkey('ctrl+f3', print, args=('triggered', 'hotkey'))
#     keyboard.press_and_release(hotkey)
#     pydirectinput.keyDown('ctrl')
#     pydirectinput.keyDown('f3')
#     pydirectinput.keyUp('f3')
#     pydirectinput.keyUp('ctrl')

    
    time.sleep(2)
