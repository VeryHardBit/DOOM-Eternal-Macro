import pyautogui as p
import time
import os
import sys
import keyboard as kb

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

i=20;
def kb_press(event):
    global i
    if event.event_type=="down":
        if event.name=="o":
            img=p.screenshot()
            img.save(f"cursors/{i:04}.tif")
            i+=1
    

if __name__=='__main__':
    kb.on_press(kb_press)
    kb.wait('m')