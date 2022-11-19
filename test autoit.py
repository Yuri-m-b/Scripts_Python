from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


import pyautogui
import pygetwindow
import gc
import time
from playsound import playsound
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #necessario para funcionar
import keyboard
import win32gui, win32ui, win32con, win32api
import autoit

a = autoit.win_get_handle("Medivia")
# Simulate the key combination Win + R to open the Run dialogue window.
autoit.win_activate("Medivia")
# autoit.control_send("Medivia", "Edit1", "LEFT")

autoit.send("{LEFT}")
