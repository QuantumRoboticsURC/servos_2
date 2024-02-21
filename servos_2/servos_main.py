
import rclpy
from std_msgs.msg import *
from adafruit_servokit import ServoKit
import time
from rclpy.node import Node

class servos_main(Node):
    def __init__(self):
        super().__init__('servos_main')
        print("Enter main")
        self.kit = ServoKit(channels=16)
        self.servo_brazo1 = 1
        self.servo_garra1 = 2
        self.servo_brazo2 = 3
        self.servo_garra2 = 4
        self.servo_cam = 5

        self.kit.servo[self.servo_brazo1].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_brazo1].actuation_range=180

        self.kit.servo[self.servo_garra1].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_garra1].actuation_range=360

        self.kit.servo[self.servo_brazo2].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_brazo2].actuation_range=180

        self.kit.servo[self.servo_garra2].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_garra2].actuation_range=360

        self.kit.servo[self.servo_cam].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_cam].actuation_range=180

        self.subscriber_brazo1 = self.create_subscription(Int8,"/ciencias/brazo1", self.callback,10)
        self.subscriber_brazo1

        self.subscriber_garra1 = self.create_subscription(Int8,"/ciencias/garra1", self.callback2,10)
        self.subscriber_garra1

        self.subscriber_brazo2 = self.create_subscription(Int8,"/ciencias/brazo2", self.callback3,10)
        self.subscriber_brazo2

        self.subscriber_garra2 = self.create_subscription(Int8,"/ciencias/garra2", self.callback4,10)
        self.subscriber_garra2

        self.subscriber_cam = self.create_subscription(Int8,"/ciencias/cam", self.callback5,10)
        self.subscriber_cam

    def limits(data, liminf,limsup):
        if data<liminf:
            data=liminf
        elif data>limsup:
            data=limsup
        return data
    def callback(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_brazo1].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
    def callback2(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_garra1].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
    def callback3(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_brazo2].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
    def callback4(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_garra2].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
    def callback5(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_cam].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
            
def main(args=None):
    rclpy.init(args=args)
    listener=servos_main()
    # spin es un nodo de ejecución que escucha a otro
    rclpy.spin(listener)
    listener.destroy_node()
    rclpy.shutdown()
    
if __name__ == '__main__':
    main()