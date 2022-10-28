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

vials = 0
i = 0
mana_full = 0


def main():
    global i
    # init window hanle
    window_name = "Medivia"
    #hwnd = win32gui.FindWindow(None, window_name)
    hwnds = find_all_windows(window_name)

    # bring each window to the front
    for hwnd in hwnds:
        win32gui.SetForegroundWindow(hwnd)
        mana_temp = mana_porcent() # Pega o valor da mana atual
        
        while(True):
            global mana_full
            while(mana_temp <= 3600):
                while(vials != 20):                 
                    if keyboard.is_pressed('esc'):
                        print("saindo")
                        break;
                    potar()
                
                if keyboard.is_pressed('esc'):
                    print("saindo")
                    exit()
                if mana_full == 1:
                    break
                refill()
            
            if keyboard.is_pressed('esc'):
                print("saindo")
                exit()
            runar()
            global i
            mana_full = 0
            i = 0
            mana_temp= mana_porcent()
            
            
                
            
    
    
    
    
    
        
def list_window_names():
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            print(hex(hwnd), '"' + win32gui.GetWindowText(hwnd) + '"')
    win32gui.EnumWindows(winEnumHandler, None)


def get_inner_windows(whndl):
    def callback(hwnd, hwnds):
        if win32gui.IsWindowVisible(hwnd) and win32gui.IsWindowEnabled(hwnd):
            hwnds[win32gui.GetClassName(hwnd)] = hwnd
        return True
    hwnds = {}
    win32gui.EnumChildWindows(whndl, callback, hwnds)
    return hwnds


def find_all_windows(name):
    result = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == name:
            result.append(hwnd)
    win32gui.EnumWindows(winEnumHandler, None)
    return result

def mana_porcent():
    mana = pyautogui.screenshot('mana.png', region=(2070,220, 40, 15))
    mana_atual = pytesseract.image_to_string(mana, config='--psm 6, -c tessedit_char_whitelist=0123456789')
    mana_int = float(mana_atual) # converte a string para int para ser usada como condicao
#     print(mana_atual)
    return (mana_int)

def runar():
    global vials
    for i in range(20):
        keyboard.press_and_release('f11')
        time.sleep(0.5)
        i = i + 1
    vials = 0
        
    
    
def refill():
    global vials
    # hi - vial - yes
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
    time.sleep(1)
    keyboard.write('20')
    time.sleep(1)
    pydirectinput.click(3070,647,button='left')
    time.sleep(0.5)
    pydirectinput.click(2835,557,button='left')
    time.sleep(0.5)
    pydirectinput.click(3130,689,button='left')
        
    # 20 mana fluid
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('f3')
    pydirectinput.keyUp('f3')
    pydirectinput.keyUp('ctrl')
    time.sleep(0.5)
    
    #yes
    pydirectinput.keyDown('ctrl')
    pydirectinput.keyDown('f4')
    pydirectinput.keyUp('f4')
    pydirectinput.keyUp('ctrl')
    time.sleep(0.5)
    
    vials = 0
    
def potar():
    #linha 1
    global vials
    global mana_full
    while vials < 20:
        time.sleep(0.35)
        pydirectinput.click(3470,450,button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3505, 450, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3540, 450, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3575, 450, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3607, 450, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        if keyboard.is_pressed('esc'):
            print("saindo")
            exit()
        pix=pyautogui.pixel(3815,116)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break
        
        #linha 2
        pydirectinput.click(3470, 485, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3505, 485, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3540, 485, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3575, 485, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3607, 485, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        if keyboard.is_pressed('esc'):
            print("saindo")
            exit()   
        pix=pyautogui.pixel(3815,116)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break

        #linha 3
        pydirectinput.click(3470, 518, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3505, 518, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3540, 518, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3575, 518, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3607, 518, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        if keyboard.is_pressed('esc'):
            print("saindo")
            exit()  
        pix=pyautogui.pixel(3815,116)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break

        #linha 4
        pydirectinput.click(3470, 553, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3505, 553, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3540, 553, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3575, 553, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1
        pydirectinput.click(3607, 553, button='right')
        time.sleep(0.35)
        pydirectinput.click(2790,480,button='left')
        time.sleep(0.35)
        vials = vials + 1   
        pix=pyautogui.pixel(3815,116)   
        if pix == (141,70,252) or pix == (137,67,251):
            mana_full = 1
            vials = 20
            break
        
        if keyboard.is_pressed('esc'):
            print("saindo")
            exit()
    
    
    
    
main()
#list_window_names()