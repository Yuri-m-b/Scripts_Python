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
import keyboard


runa_quantidade = 0

""" Alerta avisando que o pixel de vida está no lugar certo """
pix=pyautogui.pixel(3829,101)
if pix == (215,3,2) or pix == (232,23,22):
    playsound('D:\Codigos feitos por mim\Alerta3.mp3', True)

    """ pega o nome de todas as janelas abertas"""
    # print(pygetwindow.getAllTitles())
    # print(pygetwindow.getAllWindows())
    # medi = pygetwindow.getWindowsWithTitle('Steam')[0]

def runar():
    pyautogui.click(x=2797, y=25)
    keyboard.press_and_release('f11')
#     keyboard.press_and_release('f12')
    time.sleep(1.5)
    pyautogui.click(x=3470, y=322, button='right')
    pyautogui.click(x=3470, y=322, button='right')
#     pyautogui.click(x=100, y=100)
#     playsound('D:\Codigos feitos por mim\gfb.mp3', True)
    global runa_quantidade
    runa_quantidade = runa_quantidade + 1
    


def safe_zone():
    pyautogui.click(x=2797, y=25)
    pyautogui.click(x=2632, y=456)
    pyautogui.click(x=2632, y=456)
    time.sleep(1)
    keyboard.press_and_release('a')
    time.sleep(1)
    keyboard.press_and_release('a')
    
    

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

    #Sistema de defesa - caso tome hit entra no dp
    pix=pyautogui.pixel(3829,101) # pixel da barra de vida
    if pix == (16,16,16):
        pyautogui.click(x=2632, y=456)
        playsound('D:\Codigos feitos por mim\Alerta6.mp3', True)
        print("Tomou dano")
        break
    
    #Sistema de defesa - caso seja movido entra no dp
    tile = pyautogui.pixel(3658,411) # pixel na battle
    hp_bar = pyautogui.pixel(3677,79) # pixel na letra H de "Health"
    if tile != (26,26,26) and tile != (27,27,27) and tile != (26,26,26) and tile != (25,25,25) and hp_bar == (255,255,255):
        safe_zone()
        print("player on battle")        
        playsound('D:\Codigos feitos por mim\Alerta7.mp3', True)
        break
    
    if pix != (215,3,2) and pix != (16,16,16) and pix != (232,23,22): # Loop para caso tome desconnect
        print("Desconectado")
        while (hp_bar != (255,255,255)):
            time.sleep(20)
            print("Esperando ser reconectado")
            print(time.localtime())
            pyautogui.click(x=3562, y=15) #clica na aba do medivia
            keyboard.press_and_release('ENTER')            
            time.sleep(5)
            hp_bar = pyautogui.pixel(3677,79)
        print("Reconectado")
    
    manaPix = pyautogui.pixel(3665,117)
    if manaPix == (124,57,250):
        runar()
    
    manaFull = pyautogui.pixel(3695,117)   
    if manaFull == (124,57,250):
        safe_zone()    
        print("Acabou as runas")
        error = pyautogui.pixel(2784,874)
        if error == (255,255,255):
            pyautogui.click(x=2632, y=456)
            pyautogui.click(x=2632, y=456)      
            print("Acabou as runas 2")
            time.sleep(1)
        break
        
    if keyboard.is_pressed('esc'):
        print("saindo")
        break;
        playsound('D:\Codigos feitos por mim\Alerta4.mp3', True)

    
#liber espaco na memoria
    del pix
    del manaPix
    del manaFull
    del hp_bar
    gc.collect()
    time.sleep(0.5)    

#     del mana_atual
#     del mana_int
#     del tela
#     del px
#     del medi
#     print("test")

#parando codigo alerta de som
print("Foram feitas essa quantidade de runas: ", runa_quantidade)
ss = pyautogui.screenshot()
ss.show()
playsound('D:\Codigos feitos por mim\Alerta5.mp3', True)



