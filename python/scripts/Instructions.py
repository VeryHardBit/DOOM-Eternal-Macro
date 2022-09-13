import yaml
import sys
import os
from glob import glob
import keyboard as kb
import time
os.chdir(os.path.dirname(os.path.abspath(__file__))+'/..')

print(os.path.abspath(os.curdir))
all_guns=yaml.safe_load(open("config/weapons/guns.yaml").read())
print(all_guns)


class Instruction:
    def is_waiting_event(self):
        return False
    def perform(self):#return whether its parent can go into next instruction
        return False
    def is_last_instruction(self):#check from parent
        return self.parent.instructions.index(self)==len(self.parent.instructions)-1

class Sequence(Instruction):
    
    def __init__(self, *a):
        super().__init__()
        self.instructions=a
        for instruction in self.instructions:
            instruction.parent=self

        self.instruction_index=0
        self.perform_block=False
    def reset(self):
        self.instruction_index=0
        for instruction in self.instructions:
            if hasattr(instruction, "reset"):
                instruction.reset()
    def receive_event(self,event):
        #pass
        if self.perform_block==False:
            self.perform_block=True
            if hasattr(self.current_instruction(), "receive_event"):
                ready_to_next=self.current_instruction().receive_event(event)
                if ready_to_next:
                    if self.current_instruction().is_last_instruction():
                        self.instruction_index=0
                    else:
                        self.instruction_index+=1
            self.perform_block=False
    def is_waiting_event(self):
        return self.instructions[self.instruction_index].is_waiting_event()
    def current_instruction(self):
        try:
            if self.instruction_index<0:
                return None
            return self.instructions[self.instruction_index]
        except IndexError:
            return None
    def perform(self):
        if self.perform_block==False:
            self.perform_block=True
            if hasattr(self.current_instruction(), "perform"):
                while True:
                    if self.current_instruction()==None:
                        break
                    if isinstance(self.current_instruction(),Delay):
                        #print("Delay")
                        ready_to_next=self.current_instruction().perform()
                        if ready_to_next:
                            if self.current_instruction().is_last_instruction():
                                self.instruction_index=0
                            else:
                                self.instruction_index+=1
                            continue
                        else:
                            time.sleep(1/120)
                    if isinstance(self.current_instruction(), BackToStart):
                        self.instruction_index=0
                        continue
                    else:
                        ready_to_next=self.current_instruction().perform()
                        if ready_to_next:
                            if self.current_instruction().is_last_instruction():
                                #self.instruction_index=0
                                print("Meah")
                                self.instruction_index=-1
                            else:
                                self.instruction_index+=1
                        else:
                            break
            else:#maybe go into next instruction by receiving event
                pass
            self.perform_block=False
    def print(self, indent=0):
        #print("Sequence:")
        for instruction in self.instructions:
            try:
                instruction.print(indent=indent+1)
            except:
                print(f"{'  '*indent}{instruction.__class__}")


class Wait(Instruction):
    def __init__(self, *a):
        super().__init__()
        self.parent=None
        if len(a)==1:
            self.event=a[0]
        else:
            self.event=None
            self.events=[]
            self.instructions=[]
            for arg in a:
                if isinstance(arg, str):
                    self.events.append(arg.lower())
                else:
                    self.instructions.append(arg)
    def receive_event(self,event):
        if self.event!=None:
            if event==self.event:
                #print("received event "+event)
                return True
        elif self.events!=None:
            if event in self.events:
                #print("received event "+event)
                return True

    def is_waiting_event():
        return True

class Delay(Instruction):
    def __init__(self, delay):
        super().__init__()
        self.delay=delay
        self.time0=time.time()
    def perform(self):
        if self.time0==0:
            self.time0=time.time()
        if time.time()-self.time0>=self.delay:
            self.time0=0
            return True
        return False
    pass

class Do_Later(Instruction):
    def __init__(self, instruction):
        super().__init__()
        self.instruction=instruction
    def perform(self):
        self.instruction.perform()
        return True

class Switch(Instruction):
    def __init__(self, weapon_name):
        super().__init__()
        self.weapon_name=weapon_name
    @staticmethod
    def check_mod():
        pass
    def perform(self):
        #print(f"Switching to {self.weapon_name}")
        for k,v in all_guns.items():
            if k==self.weapon_name or (v["mods"]!=None and self.weapon_name in v["mods"]):
                access=v["access"].split("_")
                kb.press(access[2])
                kb.call_later(lambda k:kb.release(k), args=(access[2],),delay=1/120)
                #print(f"Switch to {access[2]}")
                return True

    pass

class Shoot(Instruction):
    def __init__(self):
        super().__init__()
    def perform(self):
        kb.press("j")
        kb.call_later(lambda k:kb.release(k), args=("j",),delay=0.1)
        #print("Performing Shot")
        return True
class Hold_Mod(Instruction):
    def __init__(self):
        super().__init__()
    def perform(self):
        kb.press("k")
        return True
class Release_Mod(Instruction):
    def __init__(self):
        super().__init__()
    def perform(self):
        kb.release("k")
        return True
class Tap(Instruction):
    def __init__(self,key):
        super().__init__()
        self.key=key
    def perform(self):
        kb.press(self.key)
        kb.call_later(lambda k:kb.release(k), args=(self.key,),delay=1/60)
        print("g pressed")
        return True
        

class Press(Instruction):
    def __init__(self,key):
        super().__init__()
        self.key=key
    def perform(self):
        kb.press(self.key)
        return True
class Release(Instruction):
    def __init__(self,key):
        super().__init__()
        self.key=key
    def perform(self):
        kb.release(self.key)
        return True



class BackToStart(Instruction):
    def __init__(self):
        super().__init__()
class Pass(Instruction):
    def __init__(self):
        super().__init__()
    pass