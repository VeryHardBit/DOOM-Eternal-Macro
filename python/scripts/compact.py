import sys
import os
import keyboard as kb
import mouse
from glob import glob
import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

kb_holding=[]
def kb_hook(event):
    global kb_holding
    k=event.name
    if event.event_type=="down":
        if k not in kb_holding:
            kb_holding.append(k)
            trigger_event(f"{event.name}_down")
        else:
            trigger_event(f"{event.name}_hold")
    elif event.event_type=="up":
        try:
            kb_holding.remove(k)
        except ValueError:
            pass
        trigger_event(f"{event.name}_release")


mouse_holding=[]
def mouse_hook(event):
    global mouse_holding
    if isinstance(event, mouse.WheelEvent):
        trigger_event('scroll_down' if event.delta < 0 else 'scroll_up')
    elif isinstance(event, mouse.ButtonEvent):
        btn=event.button
        if event.event_type=="down":
            if btn not in mouse_holding:
                mouse_holding.append(btn)
                trigger_event(f"{btn}_click")
            else:
                trigger_event(f"{btn}_hold")
        elif event.event_type=="up":#mouse_release is very captured better than mouse_down
            try:
                mouse_holding.remove(btn)
            except ValueError:
                pass
            trigger_event(f"{btn}_release")
        #print(mouse_holding)