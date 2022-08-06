import pynput

LEFT=0
RIGHT=1
MIDDLE=2
MOUSE_PRESSED_DATA={
    LEFT:False,
    RIGHT:False,
    MIDDLE:False
}


def to_pynput_button(n):
    if n==LEFT:
        return pynput.mouse.Button.left
    elif n==RIGHT:
        return pynput.mouse.Button.right
    elif n==MIDDLE:
        return pynput.mouse.Button.middle

mouse=pynput.mouse.Controller()

def mouse_hook(x, y, button, pressed):
    global MOUSE_PRESSED_DATA
    if button==pynput.mouse.Button.left:
        MOUSE_PRESSED_DATA[LEFT]=pressed
    elif button==pynput.mouse.Button.right:
        print("wtf")
        MOUSE_PRESSED_DATA[RIGHT]=pressed
    elif button==pynput.mouse.Button.middle:
        MOUSE_PRESSED_DATA[MIDDLE]=pressed
listener = pynput.mouse.Listener(on_click=mouse_hook)
listener.start()

def is_pressed(btn=LEFT):
    global MOUSE_PRESSED_DATA
    return MOUSE_PRESSED_DATA[btn]

def press(btn=LEFT):
    global MOUSE_PRESSED_DATA
    mouse.press(to_pynput_button(btn))

def release(btn=LEFT):
    global MOUSE_PRESSED_DATA
    mouse.release(to_pynput_button(btn))

def click(btn=LEFT):
    global MOUSE_PRESSED_DATA
    mouse.click(to_pynput_button(btn))