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
    time.sleep(1.5)
    pyautogui.click(x=3748, y=303, button='right')
    pyautogui.click(x=3748, y=303, button='right')
    pyautogui.click(x=100, y=100)
#     playsound('D:\Codigos feitos por mim\gfb.mp3', True) 
    
def mana_porcent():
    mana = pyautogui.screenshot('mana.png', region=(3680,110, 50, 20))
    mana_atual = pytesseract.image_to_string(mana, config='--psm 6, -c tessedit_char_whitelist=0123456789')
    mana_int = float(mana_atual) # converte a string para int para ser usada como condicao
#     print(mana_atual)
    return (mana_int)

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
    pix=pyautogui.pixel(3829,101)
    if pix == (16,16,16):
        pyautogui.click(x=3583, y=176)
        playsound('D:\Codigos feitos por mim\Alerta6.mp3', True)
        print("Tomou dano")
        break
    
    #Sistema de defesa - caso seja movido entra no dp
    tile = pyautogui.pixel(3464,167)
    if tile != (219,191,147): 
        pyautogui.click(x=3583, y=176)
        pyautogui.click(x=3583, y=176)
        print("Foi movido")
        error = pyautogui.pixel(2784,874)
        if error == (255,255,255):
            pyautogui.click(x=3583, y=192)
            pyautogui.click(x=3583, y=192)
            print("Foi movido 2")
            time.sleep(1)
            if error == (255,255,255):
                pyautogui.click(x=3624, y=208)
                pyautogui.click(x=3624, y=208)
                print("Foi movido 3")
        playsound('D:\Codigos feitos por mim\Alerta7.mp3', True)
        break
    
    if pix != (215,3,2) and pix != (16,16,16) and pix != (232,23,22):
        print("Parando codigo")
        playsound('D:\Codigos feitos por mim\Alerta4.mp3', True)
        break
    
    mana_temp = mana_porcent() # Pega o valor da mana atual
        
    if mana_temp >= 360 and mana_temp <= 400:
        runar()
        
    if mana_temp >= 400:
        pyautogui.click(x=3583, y=176)
        pyautogui.click(x=3583, y=176)
        print("Acabou as runas")
        error = pyautogui.pixel(2784,874)
        if error == (255,255,255):
            pyautogui.click(x=3583, y=192)
            pyautogui.click(x=3583, y=192)
            print("Acabou as runas 2")
            time.sleep(1)
            if error == (255,255,255):
                pyautogui.click(x=3624, y=208)
                pyautogui.click(x=3624, y=208)
                print("Acabou as runas 3")
        break
        
    if keyboard.is_pressed('esc'):
        print("saindo")
        break;
        playsound('D:\Codigos feitos por mim\Alerta4.mp3', True)

    
#liber espaco na memoria
    del pix
    del mana_temp
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


# def runar():
#     pyautogui.click(x=2757, y=25)
#     keyboard.press_and_release('f11')
#     time.sleep(1.5)
#     pyautogui.click(x=3748, y=303, button='right')
#     pyautogui.click(x=3748, y=303, button='right')
#     pyautogui.click(x=100, y=100)
#     
# def mana_porcent():
#     mana = pyautogui.screenshot('mana.png', region=(3680,110, 50, 20))
#     mana_atual = pytesseract.image_to_string(mana, config='--psm 6, -c tessedit_char_whitelist=0123456789')
#     mana_int = float(mana_atual) # converte a string para int para ser usada como condicao
# #     print(mana_atual)
#     return (mana_int)