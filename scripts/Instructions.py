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
    def receive_event():
        pass
    def is_last_instruction():
        pass
    def is_waiting_event(self):
        return self.instructions[self.instruction_index].is_waiting_event()
    def perform(self):
        self.current_index+=1
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
        self.events=[]
        for i,e in enumerate(self.events):
            self.events[i]=e.lower()
    def receive_event():
        pass
    def is_waiting_event():
        return True

class Delay(Instruction):

    pass

class Do_Later(Instruction):
    pass

class Switch(Instruction):
    def __init__(self, weapon_name):
        self.weapon_name=weapon_name
    @staticmethod
    def check_mod():
        pass
    def perform():
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