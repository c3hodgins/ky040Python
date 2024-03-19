from ky040 import ky040
from gpiozero import DigitalOutputDevice
from time import sleep

enc = ky040(15,14,18)
led = DigitalOutputDevice(4)

curState = enc.btn()
lastState = 0
led.value = 1
count = 0
last = 0
direction = 0
pwmCtr = 0
incVal = 20

with open('output.txt','w') as f:
    f.write("Encoder Count: ")
    sleep(.01)
    while(1):
        pwmCtr+=1
        last = count
        direction = enc.dir()
        if direction== 1:
            if count<999:
                count+=incVal
        elif direction == -1:
            if count>1:
                count -=incVal 
            else:
                count = 0 
        if direction !=0 and last !=count:
                f.seek(len("Encoder Count: "))
                f.write(str(count))
                f.truncate()
                f.flush()
            # print("Encoder: ",count)
        if pwmCtr < count:
            led.value = 1
        else:
            led.value = 0
        if pwmCtr>=1000:
            pwmCtr = 0
            sleep(.000000000003)