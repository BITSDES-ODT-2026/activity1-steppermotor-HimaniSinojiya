from machine import Pin
import time

in1 =Pin(27,Pin.OUT)
in2 = Pin(12,Pin.OUT)
in3 = Pin(4,Pin.OUT)
in4 = Pin(5,Pin.OUT)

pb=Pin(33,Pin.IN,Pin.PULL_UP)
pb1=Pin(19,Pin.IN,Pin.PULL_UP)

pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]


while True:
    val=pb.value()
    val1=pb1.value()
    
    if val==0:
    
        for i in range(130):
             for i in pos:
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
        
                time.sleep_ms(5)
    if val1==0:
    
        for i in range(130):
            for i in reversed(pos):
                in1.value(i[0])
                in2.value(i[1])
                in3.value(i[2])
                in4.value(i[3])
        
                time.sleep_ms(5)
    
