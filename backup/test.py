from pynput import mouse

is_mouse_pressed=False
def mouse_hook(x, y, button, pressed):
    global is_mouse_pressed
    if button==mouse.Button.left:
        is_mouse_pressed=pressed

listener = mouse.Listener(on_click=mouse_hook)
listener.start()


while True:
    print(is_mouse_pressed)