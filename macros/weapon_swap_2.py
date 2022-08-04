import yaml
import mouse
import keyboard as kb
from glob import glob
import time

combos=[]
combo=None;
weapon=None;
combo_index=0




def callback(starter_key):
    global combo
    global weapon
    global combo_index
    for combo_i in combos:
        if combo_i["starter_key"]==starter_key:
            combo=combo_i
            combo_index=0
            weapon=starter_key
            print('using combo : ',combo_i["starter_key"])
            
            return
    combo=None
def mouse_hook(event):
    global weapon
    global combo
    global combo_index
    if combo is not None:
        if isinstance(event, mouse.WheelEvent):
            weapon_list=combo["all_guns"]
            weapon=weapon_list[(weapon_list.index(weapon)+int(event.delta))%len(weapon_list)]
            print(weapon)
        if isinstance(event, mouse.ButtonEvent):
            if event.event_type==mouse.DOWN:
                switch_when=combo["switch_when"][weapon]
                cycle_guns=combo["cycle_guns"]
                if switch_when=="right left" and event.button==mouse.RIGHT:
                    print("auto left")
                    time.sleep(10/60)
                    mouse.click(mouse.LEFT)
                    time.sleep(10/60)
                    mouse.release(mouse.LEFT)
                    time.sleep(10/60)

                    combo_index=(combo_index+1)%len(cycle_guns)
                    weapon=combo["cycle_guns"][combo_index]
                    switch_when=combo["switch_when"][weapon]
                    print("2switching to",combo["cycle_guns"][combo_index],switch_when)
                    kb.press(weapon)
                    time.sleep(1/60)
                    kb.release(weapon)
                    pass
                    
                elif switch_when=="left" and event.button==mouse.LEFT:
                    pass

                    time.sleep(10/60)

                    combo_index=(combo_index+1)%len(cycle_guns)
                    weapon=combo["cycle_guns"][combo_index]
                    switch_when=combo["switch_when"][weapon]
                    print("switching to",combo["cycle_guns"][combo_index],switch_when)
                    kb.press(weapon)
                    time.sleep(1/60)
                    kb.release(weapon)
                    pass
                    
                #print(event.button,event.event_type)


if __name__=="__main__":
    for file in glob("combos/*.yaml"):
        f=open(file);
        combo_i=yaml.safe_load(f.read());
        combos.append(combo_i)
    print(combos);
    
    for combo_i in combos:
        starter_key=combo_i['starter_key']
        kb.add_hotkey(starter_key, callback,args=(starter_key,))

    mouse.hook(mouse_hook)
    kb.wait('M')