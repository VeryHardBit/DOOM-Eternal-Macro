#from win32gui import GetWindowText, GetForegroundWindow
#import time
#while True:
#    time.sleep()
#print(GetWindowText(GetForegroundWindow()))


for a in range(1,100):
    for b in range(1,100):
        if a>b:
            s1=a%b
            s2=a&(b|1)
            if s1==s2:
                print(a,b,s1,s2)