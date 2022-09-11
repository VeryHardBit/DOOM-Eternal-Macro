import yaml
import os
from Instructions import *
class Macro:
    def __init__(self,yaml_part,python_part):
        yaml_part=yaml.safe_load(yaml_part)
        yaml_part.setdefault("enabled",True)
        self.enabled=yaml_part["enabled"]
        if not self.is_enabled():
            return None
        #yaml_part.setdefault('start_when',{'weapon':'','mouse':'','keyboard':''})
        #yaml_part["start_when"].setdefault('weapon','')
        #yaml_part["start_when"].setdefault('mouse','')
        #yaml_part["start_when"].setdefault('keyboard','')


        self.start_when=yaml_part["start_when"]
        self.action=eval(python_part)
        self.type=yaml_part["macro_type"]
        self.name=yaml_part["name"]

    def is_enabled(self):
        return self.enabled
    def __str__(self):
        return f"Macro(name={self.name},start_when={self.start_when})"