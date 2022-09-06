from Instructions import *

Sequence(
    Switch("Lock-on Burst"),
    Wait(
        "right_down",
            Wait("right_release",Sequence(
                Delay(1/30),
                Switch("Super Shotgun"),
                Wait("left_release")
            )),
        "left_down",
            Wait("left_release",Sequence(
                Switch("Precision Bolt"),
                Wait("left_release")
            ))
    )
)
seq.print()
while seq.perform():
    pass
seq.receive_event("right_down")
while seq.perform():
    pass
seq.receive_event("right_release")
while seq.perform():
    pass
seq.receive_event("left_release")

seq.print()