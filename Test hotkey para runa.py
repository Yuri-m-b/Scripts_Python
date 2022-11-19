from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


import pyautogui
import pydirectinput
import pygetwindow
import gc
import time
import keyboard



def main():

    while(True):
        if keyboard.is_pressed('home'):
            print("funcionou")
            break
        
        if keyboard.is_pressed('esc'):
            print("saindo")
            break;
        

main()
