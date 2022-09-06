from Instructions import *

seq=Sequence(
    Switch("Super Shotgun"),
    Wait("left_release"),
    Switch("Ballista"),
    Wait("left_release"),
    Sequence(
        Switch("Super Shotgun"),
        Sequence(
            Wait("left_release"),
        )
    )
)
seq.print()
#seq.perform()
#seq.receive_event("left_release")
#seq.perform()
#seq.receive_event("left_release")