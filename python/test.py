from win32gui import GetWindowText, GetForegroundWindow
import time
while True:
    time.sleep()
print(GetWindowText(GetForegroundWindow()))