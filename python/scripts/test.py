from Instructions import *
import event_hooker
import keyboard as kb
import mouse
def trigger_event(event):
    print(event)
    #mouse.click()
    #time.sleep(1/120)
    #mouse.release()

if __name__=='__main__':
    event_hooker.hook(trigger_event)
    kb.wait('m')