import sys
import os
from glob import glob
import yaml
import keyboard as kb
import mouse
import time
os.chdir(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.dirname(os.path.abspath(__file__))+r'/scripts')
sys.path.append(os.path.dirname(os.path.abspath(__file__))+r'/config')

import scripts.event_hooker as event_hooker
from scripts.Macro import Macro

macros=[]
for f in glob("config/macros/*.txt"):
    f=open(f).read().split("-----")
    macro=Macro(f[0],f[1])
    if macro.is_enabled():
        macros.append(macro)
        #print(macro.action)
holding_macro=None
def trigger_event(event):
    global holding_macro
    if event=="user_mouse_m_down":
        sys.exit()
    for macro in macros:
        if "event" in macro.start_when and macro.start_when["event"]==event:
            if macro.type=="combo":
                if holding_macro is not None:
                    holding_macro.action.reset()
                holding_macro=macro
                #print(macro)
                #print(macro)
            if macro.type=="gadget":
                macro.action.perform()
    if holding_macro!=None:
        holding_macro.action.receive_event(event)
        while holding_macro.action.perform():
            pass
        #holding_macro.action.perform()
        #print(holding_macro.action.current_instruction())

if __name__=='__main__':
    event_hooker.hook(trigger_event)
    kb.wait('m')
    