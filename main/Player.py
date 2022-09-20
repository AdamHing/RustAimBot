from pynput.mouse import Controller
import time
import mouse
import pandas as pd
import numpy 
import win32api

state_left = win32api.GetKeyState(0x01)  # Left button up = 0 or 1. Button down = -127 or -128


r=3.8 #size 
t=.1333333333333333333 #time/bullet
g = 1 #use premade rel calculations


smoothing = 0
#https://www.reddit.com/r/learnpython/comments/rlkinw/how_do_i_loop_my_code_and_stop_it_with_one_key/




#TypeOfGun={"ak47","ak47c","mp5","mp5c","tompson","tompsonc","LR","LRc"}


df = pd.read_csv(r'RecoilRecordings\ak47.csv')

#def RelitiveDistance(c,gun):
def RelitiveDistance():
    # if c==1:
    #     j="c"
    #     print("crouch shooting")
    # else:
    #     j=""
    
    # if gun:
    #     df = pd.read_csv(r"RecoilRecordings\\"+"ak47"+'.csv')

    

    for i in range(0,len(df)-1):
        z = i
        if g ==False:
            xarr = df["x"].to_numpy()[z+0]-df["x"].to_numpy()[z+1]
            yarr = df["y"].to_numpy()[z+0]-df["y"].to_numpy()[z+1]
        print(type(xarr))

        if smoothing == True:
            print(xarr)
            xs= (df["x"].to_numpy()[z+0]-df["x"].to_numpy()[z+1])/2
            ys= (df["y"].to_numpy()[z+0]-df["y"].to_numpy()[z+1])/2
            
            # xs = numpy.invert(xs)
            # ys = numpy.invert(ys)
            MoveMouse(xs, ys)
            
        time.sleep(t)

        #invert array
        xarr = numpy.invert(xarr)
        yarr = numpy.invert(yarr)

        #scaling
        xarr = xarr * r
        yarr = yarr * r 
        
        print(xarr, yarr)
        MoveMouse(xarr, yarr)

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

def MoveMouse(x,y):
    damouse = Controller()
    #while True:
        #print('The current pointer position is {0}'.format(damouse.position))

    print(x,y)
    mouse._os_mouse.move_relative(x, y)


while True:
    a = win32api.GetKeyState(0x01)
    if a != state_left:  # Button state changed
        state_left = a
        print(a)

        # if (a < 0) & (keyboard.read_key() == "del"):
          
            # if keyboard.read_key() == "home":
            #     guntype = "ak47"
            # elif  keyboard.read_key() == "end":
            #     guntype = "mp5"
            # elif  keyboard.read_key() == "pgup":
            #     guntype = "tompson"
            # elif  keyboard.read_key() == "pgdn":
            #     guntype = "LR"
            
            # crouch = win32api.GetAsyncKeyState(ord('ctrl')) #detect wether the player is crouching
            # RelitiveDistance(crouch,guntype) 
            # print('Left Button Pressed')


        if (a < 0):
            #crouch = win32api.GetAsyncKeyState(ord('ctrl')) #detect wether the player is crouching
            RelitiveDistance() 
            print('Left Button Pressed')

        else:
            print('Left Button Released')   

            #win32api.SetCursorPos((midWidth, midHeight))
    time.sleep(0.001)

      