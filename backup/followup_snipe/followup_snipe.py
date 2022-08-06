import yaml
import mouse
import keyboard as kb
from glob import glob
import time
import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

combos=[]
combo=None;
weapon=None;
combo_index=0

def kb_on_press(event):
    global combo
    global weapon
    global combo_index
    for combo_i in combos:
        if combo_i["starter_key"]==event.name:
            starter_key=event.name
            combo=combo_i
            combo_index=0
            weapon=starter_key
            print('using combo : ',combo_i["starter_key"])
            return
def mouse_hook(event):
    global weapon
    global combo
    global combo_index
    if combo is not None:
        if isinstance(event, mouse.ButtonEvent):
            if event.event_type==mouse.DOWN:
        if isinstance(event, mouse.WheelEvent):
            weapon_list=combo["cycle_guns"]
            combo_index=(combo_index+int(event.delta))%len(weapon_list)
            weapon=weapon_list[combo_index]
            print(weapon)
            kb.press(weapon)
            time.sleep(1/60)
            kb.release(weapon)


if __name__=="__main__":
    for file in glob("*.yaml"):
        f=open(file);
        combo_i=yaml.safe_load(f.read());
        combos.append(combo_i)
    print(combos)

    mouse.hook(mouse_hook)
    kb.on_press(kb_on_press)
    kb.wait('M')