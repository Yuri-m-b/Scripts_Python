from PIL import Image
from PIL import ImageGrab
from functools import partial
ImageGrab.grab = partial(ImageGrab.grab, all_screens=True)


import pyautogui
#import pydirectinput
#import pygetwindow
import gc
import time
# import pytesseract
# pytesseract.pytesseract.tesseract_cmd = r'tesseract' #necessario para funcionar
# import keyboard
#import win32gui, win32ui, win32con, win32api

vials = 0
i = 0
mana_full = 0
time.sleep(3)


def main():
    global i
    # init window hanle
    mana_temp = pyautogui.pixel(1257,157)
        
    while(True):
        global mana_full
        while(mana_temp != (141,70,252)):
            while(vials != 20):
                exit = pyautogui.pixel(132,225)
                if exit != (240,173,77):
                    print("saindo")
                    break;
                potar()
            exit = pyautogui.pixel(132,225)
            if exit != (240,173,77):
                print("saindo")
                exit()
            if mana_full == 1:
                break
            refill()
        
        exit = pyautogui.pixel(132,225)
        if exit != (240,173,77):
            print("saindo")
            exit()
        runar()
        global i
        mana_full = 0
        i = 0
            

# def mana_porcent():
#     mana = pyautogui.screenshot('mana.png', region=(215,220, 40, 15))
#     mana_atual = pytesseract.image_to_string(mana, config='--psm 6, -c tessedit_char_whitelist=0123456789')
#     mana_int = float(mana_atual) # converte a string para int para ser usada como condicao
# #     print(mana_atual)
#     return (mana_int)

def runar():
    global vials
    for i in range(20):
        pyautogui.press('f11')
        time.sleep(0.5)
        pyautogui.click(910,150, button='right')
        i = i + 1
    vials = 0
        
    
    
def refill():
    global vials
    # hi = f7
    # 20 mana fluid = f8
    # yes = f9
    # offer = f10
    pyautogui.press('f7')
    time.sleep(0.5)
    pyautogui.press('f10')
    time.sleep(0.5)
    pyautogui.click(874,402) # clica para digitar
    time.sleep(1)
    pyautogui.write('20')
    time.sleep(1)
    pyautogui.click(868,508) # sell primeira janela
    time.sleep(0.5)
    pyautogui.click(632,418) # sell segunda janela
    time.sleep(0.5)
    pyautogui.click(929,550) # close
        
    # 20 mana fluid
    pyautogui.press('f8')
    time.sleep(0.5)
    # yes
    pyautogui.press('f9')
    time.sleep(0.5)
    
    
    vials = 0
    
def potar():
    #linha 1
    global vials
    global mana_full
    while vials < 20:
        time.sleep(0.6)
        pyautogui.click(910,280,button='right') #mf 1-1
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(945,280,button='right') #mf 1-2
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(980,280,button='right') #mf 1-3
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1015,280,button='right') #mf 1-4
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1050,280,button='right') #mf 1-5
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        exit = pyautogui.pixel(132,225)
        if exit != (240,173,77):
            print("saindo")
            exit()
        pix=pyautogui.pixel(1257,157)
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break
        
        #linha 2
        pyautogui.click(910,312,button='right') #mf 2-1
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(945,312,button='right') #mf 2-2
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(980,312,button='right') #mf 2-3
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1015,312,button='right') #mf 2-4
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1050,312,button='right') #mf 2-5
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        exit = pyautogui.pixel(132,225)
        if exit != (240,173,77):
            print("saindo")
            exit()  
        pix=pyautogui.pixel(1257,157)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break

        #linha 3
        pyautogui.click(910,348,button='right') #mf 3-1
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(945,348,button='right') #mf 3-2
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(980,346,button='right') #mf 3-3
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1015,348,button='right') #mf 3-4
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1050,348,button='right') #mf 3-5
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        exit = pyautogui.pixel(132,225)
        if exit != (240,173,77):
            print("saindo")
            exit() 
        pix=pyautogui.pixel(1257,157)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break

        #linha 4
        pyautogui.click(910,380,button='right') #mf 4-1
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(945,380,button='right') #mf 4-2
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(980,380,button='right') #mf 4-3
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1015,380,button='right') #mf 4-4
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pyautogui.click(1050,380,button='right') #mf 4-5
        time.sleep(0.6)
        pyautogui.click(580,338) #player
        time.sleep(0.6)
        vials = vials + 1
        pix=pyautogui.pixel(1257,157)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break
        
        exit = pyautogui.pixel(132,225)
        if exit != (240,173,77):
            print("saindo")
            exit()
       
main()
