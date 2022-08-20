import yaml
import mouse
import keyboard as kb
from glob import glob
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

combos=[]
combo=None;
macro=None;
weapon=None;
combo_index=0
#scroll_delay=10/60
scroll_delay=0
scroll_delay=5/60

switch_combo_delay=5/60
time0=0;

macros=[]

def search_macro(starter_key):
    global macros
    for macro_i in macros:
        if macro_i["starter_key"]==starter_key:
            return macro_i
    return None


def search_combo(starter_key):
    global combos
    for combo_i in combos:
        if combo_i["starter_key"]==starter_key and combo_i["enable"]==True:
            return combo_i
    return None

def kb_on_press(event):
    global combo
    global weapon
    global combo_index
    global macro



    found_combo=search_combo(event.name)
    if found_combo is not None:
        combo=found_combo
        combo_index=0
        weapon=combo["cycle_guns"][combo_index]
        print('using combo : ',combo["name"])
        kb.press(weapon)
        time.sleep(1/60)
        kb.release(weapon)
def mouse_hook(event):
    global weapon
    global combo
    global combo_index
    global time0


    if isinstance(event, mouse.WheelEvent) and not kb.is_pressed('q'):
        #if event.delta>0 and combo is not None:
        #    if time.time()-time0>=scroll_delay:
        #        time0=time.time()
        #    else:
        #        kb.press(weapon)
        #        kb.release(weapon)2
        #        return
        #    weapon_list=combo["cycle_guns"]
        #    combo_index=(combo_index+1)%len(weapon_list)
        #    weapon=weapon_list[combo_index]
        #    print(weapon)
        #    kb.press(weapon)
        #    time.sleep(1/60)
        #    kb.release(weapon)
        if event.delta<0:
            found_combo=search_combo("scroll-down")
            combo=found_combo
            combo_index=0
            weapon=combo["cycle_guns"][combo_index]
            #print('using combo : ',combo["name"])
            kb.press(weapon)
            time.sleep(1/60)
            kb.release(weapon)
        if event.delta>0:
            found_combo=search_combo("scroll-up")
            combo=found_combo
            combo_index=0
            weapon=combo["cycle_guns"][combo_index]
            #print('using combo : ',combo["name"])
            kb.press(weapon)
            time.sleep(1/60)
            kb.release(weapon)
    if isinstance(event, mouse.ButtonEvent) and not kb.is_pressed('q'):
        if event.button==mouse.LEFT:
            if event.event_type=='up' and combo is not None:
                #print('left_release')
                weapon_list=combo["cycle_guns"]
                combo_index=(combo_index+1)%len(weapon_list)
                weapon=weapon_list[combo_index]
                #print(weapon)
                kb.press(weapon)
                time.sleep(1/120)
                kb.release(weapon)
        if event.button==mouse.MIDDLE:
            if event.event_type=='up':
                found_combo=search_combo("middle-up")
                combo=found_combo
                combo_index=0
                weapon=combo["cycle_guns"][combo_index]
                #print('using combo : ',combo["name"])
                kb.press(weapon)
                time.sleep(1/120)
                kb.release(weapon)

        


if __name__=="__main__":
    for file in glob("config/*.yaml"):
        f=open(file);
        combo_i=yaml.safe_load(f.read());
        combo_i.setdefault("enable",True)
        combos.append(combo_i)
    print(combos)

    mouse.hook(mouse_hook)
    kb.on_press(kb_on_press)
    kb.wait('M')