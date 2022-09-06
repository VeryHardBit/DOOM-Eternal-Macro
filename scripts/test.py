import keyboard as kb
import mouse

def mouse_hook(event):
    if isinstance(event, mouse.ButtonEvent):
        if event.event_type=="double" or event.event_type=="down":
            print("left_down")
        if event.event_type=="up":
            print("left_up")
mouse.hook(mouse_hook)

kb.wait('esc')