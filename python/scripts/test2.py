from Instructions import *
import keyboard as kb
import mouse
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
def trigger_event(event):
    global macros
    global combo
    global weapon
    global combo_index
    global seq
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
    

