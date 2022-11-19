import win32gui, win32ui, win32con, win32api
MAIN_HWND = 0

def is_win_ok(hwnd, starttext):
    s = win32gui.GetWindowText(hwnd)
    if s.startswith(starttext):
            print (s)
            global MAIN_HWND
            MAIN_HWND = hwnd
            return None
    return 1


def find_main_window(starttxt):
    global MAIN_HWND
    win32gui.EnumChildWindows(0, is_win_ok, starttxt)
    return MAIN_HWND


def winfun(hwnd, lparam):
    s = win32gui.GetWindowText(hwnd)
    if len(s) > 3:
        print("winfun, child_hwnd: %d   txt: %s" % (hwnd, s))
    return 1

def main():
    main_app = 'Medivia'
    hwnd = win32gui.FindWindow(None, main_app)
    print (hwnd)
    if hwnd < 1:
        hwnd = find_main_window(main_app)
    print (hwnd)
    if hwnd:
        print(win32gui.EnumChildWindows(hwnd, winfun, None))

main()