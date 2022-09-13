#InstallMouseHook


#IfWinActive DOOMEternal
WheelDown::
Send Numpad5
KeyWait, LButton
Send Numpad2
KeyWait, RButton,D
KeyWait, LButton,D
KeyWait, LButton
return

#IfWinActive DOOMEternal
WheelUp::
Send 6
return

#IfWinActive DOOMEternal
MButton::
Send 4
return
