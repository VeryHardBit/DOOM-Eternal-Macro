import sys
import os
from glob import glob
import yaml
import keyboard as kb
import mouse
import time
from win32gui import GetWindowText, GetForegroundWindow
from pathlib import Path

main_dir=os.path.dirname(os.path.abspath(__file__))
config_dir=main_dir+"/config"
HOME=Path.home()
data={}
data['main_dir']=main_dir
with open(f'{HOME}/.DOOM-Eternal-Macro','w') as f:
    f.write(yaml.dump(data))


os.chdir(main_dir)
sys.path.append(f'{main_dir}/scripts')
#sys.path.append(f'{macro_dir}/config')



DEBUG=False
import scripts.event_hooker as event_hooker
from scripts.Macro import Macro

macros=[]
for f in glob("config/macros/*.txt"):
    f=open(f).read().split("-----")
    macro=Macro(f[0],f[1])
    if macro.is_enabled():
        macros.append(macro)
        #print(macro.action)
holding_macro0=None
holding_macro=None
holding_macro_time=None
holding_macro_cooldown=0
_temp=False
def trigger_event(event):
    global holding_macro
    global DEBUG
    global _temp
    global holding_macro0
    global holding_macro_time
    global holding_macro_cooldown
    if event=="user_mouse_m_down":
        sys.exit()
    if _temp==False:
        print("This should appear")
        print(event)
        _temp=True
    if GetWindowText(GetForegroundWindow())=="DOOMEternal" or True:
        #There is macro combo,single weapon,macro perform once
        if event=="user_keyboard_q_down" or event=="user_keyboard_q_release":
            holding_macro=None
        for macro in macros:
            if "event" in macro.start_when and macro.start_when["event"]==event:
                #print(macro)
                macro.DEBUG=DEBUG
                if macro.type=="combo":
                    if holding_macro is not None:
                        if time.time()-holding_macro_time>=holding_macro_cooldown:
                            holding_macro.action.reset()
                            holding_macro0=holding_macro
                            holding_macro=macro
                            holding_macro_time=time.time()
                            holding_macro_cooldown=holding_macro.cooldown
                    else:
                        holding_macro0=holding_macro
                        holding_macro=macro
                        holding_macro_time=time.time()
                        holding_macro_cooldown=holding_macro.cooldown
                    #print(macro)
                if macro.type=="gadget":
                    macro.action.reset()
                    macro.action.perform()
        if holding_macro!=None:
            holding_macro.action.receive_event(event)
            while holding_macro.action.perform():
                pass

if __name__=='__main__':
    event_hooker.hook(trigger_event)
    event_hooker.map_event(yaml.safe_load(open(f"{config_dir}/event_map.yaml").read()))
    kb.wait('m')
    