import keyboard as kb
import mouse
import yaml
import os
from pathlib import Path

#HOME=Path.home()
#data={}
#with open(f'{HOME}/.DOOM-Eternal-Macro','r') as f:
#    data=yaml.safe_load(f.read())
#macro_dir=data['macro_dir']



kb_holding=[]
def kb_hook(event):
    global kb_holding
    global trigger_fn
    global event_mapper
    k=event.name
    #print(k)
    evt=f"keyboard_{k}"
    if evt in event_mapper:
        evt=event_mapper[evt]
    if event.event_type=="down":
        if k not in kb_holding:
            evt=f"user_{evt}_down"
            kb_holding.append(k)
        else:
            evt=f"user_{evt}_hold"
    elif event.event_type=="up":
        evt=f"user_{evt}_release"
        if k in kb_holding:
            kb_holding.remove(k)
    trigger_fn(evt)
    #if event.event_type=="down":
    #    if k not in kb_holding:
    #        kb_holding.append(k)
    #        
    #        trigger_fn(f"user_{evt}_down")
    #    else:
    #        trigger_fn(f"user_{evt}_hold")
    #elif event.event_type=="up":
    #    try:
    #        kb_holding.remove(k)
    #    except ValueError:
    #        pass
    #    trigger_fn(f"user_keyboard_{k}_release")
mouse_holding=[]
def mouse_hook(event):
    global mouse_holding
    global trigger_fn
    global event_mapper
    evt="mouse_"

    if isinstance(event, mouse.WheelEvent):
        evt+='scroll_down' if event.delta < 0 else 'scroll_up'
        if evt in event_mapper:
            evt=event_mapper[evt]
    elif isinstance(event, mouse.ButtonEvent):
        evt+=f"{event.button}"
        if evt in event_mapper:
            evt=event_mapper[evt]
        if event.event_type=="down" or event.event_type=="double":
            evt+="_down"
        elif event.event_type=="up":
            evt+="_release"
    else:
        return
    evt=f"user_{evt}"
    trigger_fn(evt)
trigger_fn=None
def hook(fn):
    global trigger_fn
    trigger_fn=fn

event_mapper={}
def map_event(data):
    global event_mapper
    event_mapper=data

mouse.hook(mouse_hook)
kb.hook(kb_hook)