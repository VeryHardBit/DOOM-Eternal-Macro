import sys
import os
from glob import glob
import yaml
import keyboard as kb

os.chdir(os.path.dirname(os.path.abspath(__file__)))
from scripts.Instructions import *
import scripts.event_hooker

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
    event_hooker.hook(trigger_event)
    kb.wait('m')
    