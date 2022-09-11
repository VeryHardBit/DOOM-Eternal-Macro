import keyboard as kb
import mouse

kb_holding=[]
def kb_hook(event):
    global kb_holding
    global trigger_fn
    k=event.name
    if k=='f':
        k='mod'
    if event.event_type=="down":
        if k not in kb_holding:
            kb_holding.append(k)
            trigger_fn(f"user_keyboard_{k}_down")
        else:
            trigger_fn(f"user_keyboard_{k}_hold")
    elif event.event_type=="up":
        try:
            kb_holding.remove(k)
        except ValueError:
            pass
        trigger_fn(f"user_keyboard_{k}_release")
mouse_holding=[]
def mouse_hook(event):
    global mouse_holding
    global trigger_fn
    if isinstance(event, mouse.WheelEvent):
        t='scroll_down' if event.delta < 0 else 'scroll_up'
        trigger_fn(f"user_mouse_{t}")
    elif isinstance(event, mouse.ButtonEvent):
        btn=event.button
        
        if event.event_type=="down" or event.event_type=="double":
            if btn not in mouse_holding:
                mouse_holding.append(btn)
                trigger_fn(f"user_mouse_{btn}_down")
            #else:
            #    trigger_fn(f"user_mouse_{btn}_hold")
        elif event.event_type=="up":#mouse_release is very captured better than mouse_down
            try:
                mouse_holding.remove(btn)
            except ValueError:
                pass
            trigger_fn(f"user_mouse_{btn}_release")
trigger_fn=None
def hook(fn):
    global trigger_fn
    trigger_fn=fn

mouse.hook(mouse_hook)
kb.hook(kb_hook)