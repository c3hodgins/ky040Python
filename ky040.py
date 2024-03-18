import gpiozero
from gpiozero import  GPIODevice,DigitalInputDevice,DigitalOutputDevice
from time import sleep

class ky040:

    def __init__(self, CLK, DT, SW):
        self.A = DigitalInputDevice(CLK)
        self.B = DigitalInputDevice(DT)
        self.C = DigitalInputDevice(SW)
        self.num = 0
        self.prevA = 0
        self.prevB = 0
        self.currA = 0
        self.currB = 0
    def btn(self):
        return self.C.value
    def dir(self):
        num = 0
        
        self.prevA = self.currA
        self.prevB = self.currB
        self.currA = self.A.value
        self.currB = self.B.value
        if self.prevA == 0 and self.prevB == 0:
            if self.currA ==1 and self.currB == 0:
                num=1
            elif self.currB == 1 and self.currA == 0:
                num=-1
        return num
# count = 0
# enc = ky040(15,14,18)
# while(True):
#     direction = enc.dir()
#     if direction == 1:
#         count+=1
#     elif direction == -1:
#         count-=1
    
#     if direction!= 0:
#         print(count)