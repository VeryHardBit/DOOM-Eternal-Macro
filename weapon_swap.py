import mouse
import keyboard as kb
import time




class Weapon:
    def __init__(self):
        self.next_weapon = None
        self.click_delay=0.1
        pass
    def is_swapping_ready(self):
        pass
    def swap(self):
        pass
    def get_name(self):
        return self.__class__.__name__
    pass

class CombatShotgun:
    def __init__():
        pass
    def is_swap_ready():
        if mouse.is_pressed(mouse.LEFT) and mouse.is_pressed(mouse.RIGHT):
            time.sleep(self.click_delay)
            return True
class HeavyCannon:#mainly precision bolt
    def __init__():
        pass
    def is_swap_ready():
        if mouse.is_pressed(mouse.LEFT) and mouse.is_pressed(mouse.RIGHT):
            time.sleep(self.click_delay)
            return True
class PlasmaRifle:
    pass
class RocketLauncher:
    def is_swap_ready():
        if mouse.is_pressed(mouse.LEFT):
            time.sleep(self.click_delay)
            return True
class SuperShotgun:
    def is_swap_ready():
        if mouse.is_pressed(mouse.LEFT):
            time.sleep(self.click_delay)
            return True
class Ballista:
    def is_swap_ready():
        if mouse.is_pressed(mouse.LEFT):
            time.sleep(self.click_delay)
            return True
class ChainGun:
    pass
class BFG9000:
    pass
class Crucible:
    pass
class Unmakyr:
    pass
class UnknownWeapon:
    #wait for keys only
    pass

current_weapon = None
weapons_dict={
    "1": CombatShotgun(),
    "2": HeavyCannon(),
    "3": PlasmaRifle(),
    "4": RocketLauncher(),
    "5": SuperShotgun(),
    "6": Ballista(),
    "7": ChainGun(),
    "8": BFG9000(),
    "V": Crucible(),
    "9": Unmakyr(),
    "M": UnknownWeapon(),
}
def on_user_press_swap_key(key):
    global current_weapon
    current_weapon = weapons_dict[key]




def main():
    global current_weapon
    global weapons_dict

    weapons_dict["1"].next_weapon = weapons_dict["2"]
    weapons_dict["2"].next_weapon = weapons_dict["4"]
    weapons_dict["4"].next_weapon = weapons_dict["5"]
    weapons_dict["5"].next_weapon = weapons_dict["6"]
    weapons_dict["6"].next_weapon = weapons_dict["1"]
    for key,weapon_i in weapons_dict.items():
        kb.add_hotkey(k, on_user_press_swap_key,args=(key,))
        print(k,weapon_i.get_name())

if __name__=='__main__':
    main()