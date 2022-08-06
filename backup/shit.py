import keyboard as kb
import mouse
import time



import mouse_manipulator as mouse



weapons_list=[
    "5","2","6","2"
]
combo_index=0
kb.wait('n')
while True:
    b=mouse.is_pressed(mouse.LEFT)
    print(b)
    if b:
        weapon=weapons_list[combo_index]
        kb.press(weapon)
        time.sleep(1/60)
        kb.release(weapon)

        if weapon=="2":
            mouse.press(mouse.RIGHT)
            time.sleep(31/60)
            mouse.click(mouse.LEFT)
            time.sleep(20/60)
            mouse.release(mouse.RIGHT)
            combo_index=(combo_index+1)%len(weapons_list)
        elif weapon=="6":
            time.sleep(25/60)
            mouse.click()
            time.sleep(1/60)
            combo_index=(combo_index+1)%len(weapons_list)
            weapon=weapons_list[combo_index]
            kb.press(weapon)
            time.sleep(25/60)
            
            
        else:

            time.sleep(25/60)
            mouse.click()
            time.sleep(5/60)
            combo_index=(combo_index+1)%len(weapons_list)
        
    if kb.is_pressed('m'):
        break
    time.sleep(1/60)
    