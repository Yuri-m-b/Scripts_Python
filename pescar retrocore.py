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



time.sleep(3)

#Tira print da tela dos 2 monitores
while(True):
    """!
    #https://pillow.readthedocs.io/en/stable/reference/ImageGrab.html
    #https://pixspy.com/  - para pegar as coordenadas
    #https://play.ht/text-to-speech-online/
    Cores do client
    # pix rgb (215,3,2) = Full Life
    # (26,26,26) = Perdeu Vida
    """
#     tela = ImageGrab.grab(include_layered_windows = False, all_screens=True)
#     px = tela.load()
# tela.show()
# print (tela.size)
    
    pyautogui.click(x=785, y=454, button='right') #clicando na vara
    time.sleep(1)
    pyautogui.click(x=775, y=367)
    time.sleep(1)
    pyautogui.click(x=785, y=454, button='right')
    time.sleep(1)
    pyautogui.click(x=700, y=367)
    time.sleep(1)
        
        
    if keyboard.is_pressed('esc'):
        print("saindo")
        break;
        playsound('D:\Codigos feitos por mim\Alerta4.mp3', True)

    
#liber espaco na memoria
    gc.collect()
    time.sleep(0.5)    

#     del mana_atual
#     del mana_int
#     del tela
#     del px
#     del medi
#     print("test")

#parando codigo alerta de som
playsound('D:\Codigos feitos por mim\Alerta5.mp3', True)   


