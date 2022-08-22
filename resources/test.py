import keyboard as kb
def kb_hook(event):
    print(event,event.event_type)
kb.hook(kb_hook)
kb.wait('M')