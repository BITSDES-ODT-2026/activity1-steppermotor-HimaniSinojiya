from machine import Pin
import time

in1 =Pin(27,Pin.OUT)
in2 = Pin(12,Pin.OUT)
in3 = Pin(4,Pin.OUT)
in4 = Pin(5,Pin.OUT)

pos = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1],]

for i in range(1000):
     for i in pos:
        in1.value(i[0])
        in2.value(i[1])
        in3.value(i[2])
        in4.value(i[3])
        
        time.sleep_ms(5)
        
in1.value(0)
in2.value(0)
in3.value(0)
in4.value(0)
