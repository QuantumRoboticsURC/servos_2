
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
        self.servo_camArm = 7
        self.servo_camAntena = 4
        self.servo_rotacion = 3
        self.kit.servo[self.servo_camArm].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_camArm].actuation_range=180
        self.kit.servo[self.servo_camAntena].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_camAntena].actuation_range=180
        self.kit.servo[self.servo_rotacion].set_pulse_width_range(500,2500)
        self.kit.servo[self.servo_rotacion].actuation_range=642
        self.kit.servo[self.servo_camArm].angle=100
        self.kit.servo[self.servo_camAntena].angle=45
        self.kit.servo[self.servo_rotacion].angle=170
        self.subscriber_cam = self.create_subscription(Int32,"/arm_teleop/cam", self.callback,10)
        self.subscriber_cam
        self.subscriber_camA = self.create_subscription(Int32,"/arm_teleop/camA", self.callback2,10)
        self.subscriber_camA
        self.subscriber_servo_gripper = self.create_subscription(Int32,"/arm_teleop/servo_gripper", self.callback3,10)
        self.subscriber_servo_gripper
    def limits(self,data, liminf,limsup):
        if data<liminf:
            data=liminf
        elif data>limsup:
            data=limsup
        return data
    def callback(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_camArm].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
    def callback2(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.servo_camAntena].angle = int(ndata)        
        except Exception as e:
            print(data.data)
            print(e)
    def callback3(self,data):
        try:
            ndata=self.limits(data.data,0,300)
            self.kit.servo[self.servo_rotacion].angle = int(ndata)        
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
