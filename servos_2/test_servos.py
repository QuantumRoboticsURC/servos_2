#!/usr/bin/env python3

from adafruit_servokit import ServoKit

kit = ServoKit(channels=16)
s = 4
kit.servo[s].set_pulse_width_range(500, 2400)
kit.servo[s].actuation_range=642
state = True
while state:
    angle = int(input("Ingrese el ángulo: "))
    kit.servo[s].angle = angle
    if(int(input("¿Quiere seguir? 1/0: "))==0):
        state=False