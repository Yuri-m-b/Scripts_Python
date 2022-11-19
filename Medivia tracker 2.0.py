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

#http://www.kbdedit.com/manual/low_level_vk_list.html
VK_KEY_A = 0x41


def main():
    
#     list_window_names()
    window_name = "Medivia"
    #hwnd = win32gui.FindWindow(None, window_name)
    hwnds = find_all_windows(window_name)
    print(hwnds)
    

    # bring each window to the front
    for hwnd in hwnds:
        print("for")
        win32gui.SetForegroundWindow(hwnd)
        press_key(hwnd, VK_KEY_A)
        
    press_key(hwnd, VK_KEY_A)
        


def press_key(hwnd, key):
    win32api.SendMessage(hwnd, win32con.WM_KEYDOWN, key, 0)
    time.sleep(1)
    win32api.SendMessage(hwnd, win32con.WM_KEYUP, key, 0)
    print("apertou")


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


main()
