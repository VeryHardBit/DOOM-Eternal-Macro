import yaml
import mouse
import keyboard as kb
from glob import glob
import time
import os
import pyautogui as p
import pydirectinput as pdi
os.chdir(os.path.dirname(os.path.abspath(__file__)))
DEBUG=False
def log(*s):
    if DEBUG:
        print(*s)





all_weapons=None
macros=[]
gadget=None
combo=None
combo_index=0
weapon=None
#scroll_delay=10/60
scroll_delay=0
scroll_delay=5/60

switch_combo_delay=5/60
time0=0;

combo_start_time=0






def search_macro(starter_key):
    global macros
    for macro_i in macros:
        if macro_i["starter_key"]==starter_key and macro_i["enable"]==True:
            return macro_i
    return None
def kb_hook(event):
    global combo
    global weapon
    global combo_index
    global prev_key
    global combo_start_time
    if event.event_type!="down":
        return
    found_macro=search_macro(event.name)
    if found_macro is not None:
        if combo is not None:
            if found_macro==combo:
                if time.time()-combo_start_time>1:#This is single press
                    pass
                else:#technically you're double press it!
                    found_macro=search_macro(f"{event.name}-double")
                    combo_start_time=time.time()
                    combo=found_macro
                    combo_index=0
                    weapon=combo["cycle_guns"][combo_index]
                    log('using combo : ',combo["name"])
                    kb.press(weapon)
                    kb.call_later(lambda k:kb.release(k), args=(weapon), delay=1/120)
                    return
        if found_macro["macro_type"]=="combo":
            combo_start_time=time.time()
            combo=found_macro
            combo_index=0
            weapon=combo["cycle_guns"][combo_index]
            log('using combo : ',combo["name"])
            kb.press(weapon)
            kb.call_later(lambda k:kb.release(k), args=(weapon), delay=1/120)
        if found_macro["macro_type"]=="gadget":
            for action,v in found_macro["auto_action"]:
                if action=="rotate":
                    #mouse.move(v, 0,absolute=False,duration=0.1)
                    #p.move(v, 0)
                    time.sleep(0.1)
                    pdi.move(v,0)
                    #time.sleep(0.1)
                if action=="press":
                    kb.call_later(lambda k:kb.press(k), args=(v), delay=2/120)
                    kb.call_later(lambda k:kb.release(k), args=(v), delay=4/120)



    
def mouse_hook(event):
    global weapon
    global combo
    global combo_index
    global time0

    found_combo=None


    if isinstance(event, mouse.WheelEvent) and not kb.is_pressed('q'):
        if event.delta<0:
            for k in all_weapons:
                if kb.is_pressed(k):
                    found_combo=search_macro(f"{k} & scroll-down")
            if found_combo is None:
                found_combo=search_macro("scroll-down")
            combo_start_time=time.time()
            combo=found_combo
            combo_index=0
            weapon=combo["cycle_guns"][combo_index]
            log('using combo : ',combo["name"])
            kb.press(weapon)
            kb.call_later(lambda k:kb.release(k), args=(weapon), delay=1/60)
        if event.delta>0:
            for k in all_weapons:
                if kb.is_pressed(k):
                    found_combo=search_macro(f"{k} & scroll-up")
            if found_combo is None:
                found_combo=search_macro("scroll-up")
            combo_start_time=time.time()
            combo=found_combo
            combo_index=0
            weapon=combo["cycle_guns"][combo_index]
            log('using combo : ',combo["name"])
            kb.press(weapon)
            kb.call_later(lambda k:kb.release(k), args=(weapon), delay=1/60)
    if isinstance(event, mouse.ButtonEvent) and not kb.is_pressed('q'):
        if event.button==mouse.LEFT:
            if event.event_type=='up' and combo is not None:
                #print('left_release')
                weapon_list=combo["cycle_guns"]
                combo_index=(combo_index+1)%len(weapon_list)
                weapon=weapon_list[combo_index]
                #print(weapon)
                kb.press(weapon)
                kb.call_later(lambda k:kb.release(k), args=(weapon), delay=1/120)
        if event.button==mouse.MIDDLE:
            if event.event_type=='up':
                combo_start_time=time.time()
                found_combo=search_macro("middle-release")
                combo=found_combo
                combo_index=0
                weapon=combo["cycle_guns"][combo_index]
                log('using combo : ',combo["name"])
                kb.press(weapon)
                kb.call_later(lambda k:kb.release(k), args=(weapon), delay=1/120)

        


if __name__=="__main__":
    all_weapons=yaml.safe_load(open("config/all-weapons.yaml").read())
    files=glob("config/*.yaml")
    print(files)
    files.remove("config\\all-weapons.yaml");
    for file in files:
        f=open(file);
        macro_i=yaml.safe_load(f.read());
        macro_i.setdefault("enable",True)
        macro_i["starter_key"]=macro_i["starter_key"].lower()
        if macro_i["enable"]==True:
            macros.append(macro_i)
    print(macros)

    mouse.hook(mouse_hook)
    kb.hook(kb_hook)
    time0=time.time()
    kb.wait('M')