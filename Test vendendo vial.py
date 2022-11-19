from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


import pyautogui
import pydirectinput
import pygetwindow
import gc
import time
from playsound import playsound
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #necessario para funcionar
import keyboard
import win32gui, win32ui, win32con, win32api


time.sleep(1)

pydirectinput.keyDown('ctrl')
pydirectinput.keyDown('f2')
pydirectinput.keyUp('f2')
pydirectinput.keyUp('ctrl')
time.sleep(0.5)
pydirectinput.keyDown('ctrl')
pydirectinput.keyDown('f5')
pydirectinput.keyUp('f5')
pydirectinput.keyUp('ctrl')
time.sleep(0.5)
pydirectinput.click(3076,540,button='left')
# time.sleep(1)
# keyboard.press_and_release('del')
time.sleep(1)
keyboard.write('20')
time.sleep(1)
pydirectinput.click(3070,647,button='left')
time.sleep(0.5)
pydirectinput.click(2835,557,button='left')
time.sleep(0.5)
pydirectinput.click(3130,689,button='left')

# keyboard.write('20')
