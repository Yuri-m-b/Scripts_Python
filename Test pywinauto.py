from pywinauto.application import Application
import time
import warnings
warnings.simplefilter('ignore', category=UserWarning)

def main():
    app = Application()
    app.connect(title_re='Medivia')
    win = app.window(title_re = "Medivia")
    
    test = (715,478)
    
    win.click("left", coords= test)
    win.click("left", coords= test)
    win.click("left", coords= test)
    win.click("left", coords= test)
    win.click("left", coords= test)
    win.click("left", coords= test)
    
main()