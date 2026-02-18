from machine import Pin
import time

in1 =Pin(27,Pin.OUT)
in2 = Pin(12,Pin.OUT)
in3 = Pin(4,Pin.OUT)
in4 = Pin(5,Pin.OUT)

pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],]

while True:
    for i in range(500):
         for i in pos:
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
        
            time.sleep_ms(5)

        
    for i in range(500):
        for i in reversed(pos):
            in1.value(i[0])
            in2.value(i[1])
            in3.value(i[2])
            in4.value(i[3])
        
        
            time.sleep_ms(5)
        
