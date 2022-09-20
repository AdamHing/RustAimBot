from pynput.keyboard import Listener
import time
import win32api
import keyboard
state_left = win32api.GetKeyState(0x01)

def RelitiveDistance(gun):
    c=0
    if c==1:
        j="c"
        print("crouch shooting")
    else:
        j=""
    print(j)
    print(gun)
    for i in range(0,30):
        state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128
        a = win32api.GetKeyState(0x01)
        if a == state_left:  # Button state changed
            state_left != a
            print(a)
            if a < 0:
                print('Left Button Pressed')
            else:
                print('Left Button Released')
                break
        time.sleep(.133333)




def on_press(key):  # The function that's called when a key is pressed
    print(key)



while True:
    a = win32api.GetKeyState(0x01)
    if a != state_left:  # Button state changed
        state_left = a
        print("test1")
       
        if keyboard.read_key() == "home":
            guntype = "ak47"
            print("test2")
        elif  keyboard.read_key() == "end":
            guntype = "mp5"
        elif  keyboard.read_key() == "pgup":
            guntype = "tompson"
        elif  keyboard.read_key() == "pgdn":
            guntype = "LR"

        #crouch = win32api.GetAsyncKeyState(ord('ctrl')) #detect wether the player is crouching

        RelitiveDistance(guntype) 

    time.sleep(0.001)