class Instruction:
    def is_waiting_event(self):
        return False

class Sequence(Instruction):
    def __init__(self, *a):
        super().__init__()
        self.instructions=a
        for instruction in self.instructions:
            instruction.parent=self

        self.instruction_index=0
    def receive_event(self,event):
        if hasattr(self.current_instruction(), "receive_event"):
            if self.current_instruction().receive_event(event)==True:
                self.instruction_index+=1
    def is_last_instruction():
        pass
    def is_waiting_event(self):
        return self.instructions[self.instruction_index].is_waiting_event()
    def current_instruction(self):
        return self.instructions[self.instruction_index]
    def perform(self):
        if hasattr(self.current_instruction(), "perform"):
            self.current_instruction().perform()
            self.instruction_index+=1
        else:#maybe go into next instruction by receiving event
            pass
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
            for i,e in enumerate(self.events):
                self.events[i]=e.lower()
    def receive_event(self,event):
        if self.event!=None:
            if event==self.event:
                print("received event "+event)
                return True
    def is_waiting_event():
        return True
    def perform(self):
        return False

class Delay(Instruction):
    def __init__(self, delay):
        super().__init__()
        self.delay=delay
        self.time=0
    def perform(self):
        self.time+=1/30
        if self.time>=self.delay:
            self.time=0
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
        self.weapon_name=weapon_name
    @staticmethod
    def check_mod():
        pass
    def perform(self):
        print(f"Switching to {self.weapon_name}")
        pass
    pass

class Press(Instruction):
    pass

class Release(Instruction):
    pass



class BackToStart(Instruction):
    pass
class Pass(Instruction):
    pass