import pyautogui
import pygetwindow

import win32gui, win32ui, win32con, win32api
import keyboard
import autoit
import time

# http://www.kbdedit.com/manual/low_level_vk_list.html
VK_KEY_W = 0x57
VK_KEY_A = 0x41
VK_KEY_S = 0x53
VK_KEY_D = 0x44
VK_KEY_P = 0x50
VK_SHIFT = 0xA0

def main():
    # init window hanle
    window_name = "Medivia"
    #hwnd = win32gui.FindWindow(None, window_name)
    hwnds = find_all_windows(window_name)

    # bring each window to the front
    for hwnd in hwnds:
        win32gui.SetForegroundWindow(hwnd)

    for hwnd in hwnds:
# #         autoit.send("{LEFT}")
# #         time.sleep(1)
# #         autoit.send("{Right}")
# #         time.sleep(1)
# #         autoit.send("{LEFT}")
# #         time.sleep(1)
# #         autoit.send("{Right}")
# #         time.sleep(10)
#         time.sleep(1)
#         pyautogui.click(x=3470, y=450, button='right')
#         time.sleep(0.5)
#         pyautogui.click(x=2780, y=475, button='left')
        autoit.control_click("left",272,70)

#     time.sleep(1)
#     pyautogui.click(x=3470, y=450, button='right')
#     time.sleep(0.5)
#     pyautogui.click(x=2780, y=475, button='left')
#     autoit.control_click("right, 3470, 450, 0")
    



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
#list_window_names()