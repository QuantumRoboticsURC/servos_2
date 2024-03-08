#!/usr/bin/env python3

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
s = 4
print(s)
kit.servo[s].set_pulse_width_range(1000, 2000)
kit.servo[s].actuation_range=180
state = True
while state:
    angle = int(input("Ingrese el ángulo: "))
    kit.continuous_servo[s].throttle = angle
    if(int(input("¿Quiere seguir? 1/0: "))==0):
        state=False
