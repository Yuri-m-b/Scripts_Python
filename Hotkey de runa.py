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
        
#         print("entrou")
        #Pega as coordenadas do mouse
        if keyboard.is_pressed('home'):
            print("Pegou posicao do mouse")
            position_1 = pydirectinput.position()
            time.sleep(0.5)
            print(position_1)
#             print(position_1[0])
        
        #Recebe a posição atual do mouse, clica na runa, solta o mouse na posição que ele estava.
        if keyboard.is_pressed('insert'):
            position_2 = pydirectinput.position()
            pydirectinput.click(position_1[0],position_1[1],button='right')
            pydirectinput.moveTo(position_2[0],position_2[1])     
        
        if keyboard.is_pressed('esc'):
            print("saindo")
            break;
        

main()

