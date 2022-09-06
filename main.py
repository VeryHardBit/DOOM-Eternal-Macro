import sys
import os
import keyboard as kb
import mouse
from glob import glob
import yaml

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.abspath(__file__)))
from scripts.Gadget import *
from scripts.Weapon import *

kb_holding=[]
def kb_hook(event):
    global kb_holding
    k=event.name
    if k=='f':
        k='mod'
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
        if event.event_type=="down" or event.event_type=="double":
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
    
class Weapon():
    def __init__():
        pass
weapons=yaml.safe_load(open("config/weapons/guns.yaml"))
#macro sorting order:
#   start_when with current_weapon
#   start_when with mouse
#   start_when with keyboard
macros=[]#sorting order
for f in glob("config/macros/*.yaml"):
    macro=yaml.safe_load(open(f))
    macro.setdefault('enabled',True)
    if macro['enabled']:
        macro.setdefault('start_when',{'weapon':'','mouse':'','keyboard':''})
        macro["start_when"].setdefault('weapon','')
        macro["start_when"].setdefault('mouse','')
        macro["start_when"].setdefault('keyboard','')
        macros.append(macro)
    #macros.append(yaml.safe_load(open(f)))
combo=None
combo_index=0

def get_access(name):#name can be mod-name or weapon-name
    global weapons
    if name in weapons:
        return weapons[name]["access"]
    for k,v in weapons.items():
        if name in v["mods"]:
            return v["access"]
    return None
def check_mod():#use image recognition to get mod name
    pass 

def trigger_event(event):
    global macros
    global combo
    global weapon
    global combo_index
    event=event.lower()
    #print(event)
    #check for macro 
    for macro in macros:
        if event==macro['start_when']["keyboard"] or event==macro['start_when']["mouse"] or event=='mod_down':
            if macro['macro_type']=="combo":
                combo=macro
                combo_index=0
                weapon=combo['cycle_guns'][combo_index]
                k=get_access(weapon).split('_')[0]
                kb.press(k)
                kb.call_later(lambda x:kb.release(x),args=(k),delay=1/120)
                print(combo)
                break
            if macro['macro_type']=="standalone_weapon":
                combo=None
                break
    #check for combo
    if combo is not None:
        if weapon in combo['next_weapon_when']:
            if event==combo['next_weapon_when'][weapon]:
                combo_index=(combo_index+1)%len(combo['cycle_guns'])
                weapon=combo['cycle_guns'][combo_index]
                k=get_access(weapon).split('_')[0]
                kb.press(k)
                kb.call_later(lambda x:kb.release(x),args=(k),delay=1/120)
                #print(weapon)
        pass


if __name__=='__main__':
    kb.hook(kb_hook)
    mouse.hook(mouse_hook)
    kb.wait('m')
    