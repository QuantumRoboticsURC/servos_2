
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

        self.servo_camArm = 5
        self.servo_camAntena = 6
        self.servo_rotacion = 7
        
        self.kit.servo[self.servo_camArm].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_camArm].actuation_range=180
        
        self.kit.servo[self.servo_camAntena].set_pulse_width_range(500,2400)
        self.kit.servo[self.servo_camAntena].actuation_range=180
        
        self.kit.servo[self.servo_rotacion].set_pulse_width_range(500,2500)
        self.kit.servo[self.servo_rotacion].actuation_range=642
        
        self.kit.servo[self.servo_camArm].angle=100
        self.kit.servo[self.servo_camAntena].angle=45
        self.kit.servo[self.servo_rotacion].angle=170
        
        self.subscriber_camArm = self.create_subscription(Int32,"/arm_teleop/camArm", self.callback,10)
        self.subscriber_camArm
        
        self.subscriber_camAntena = self.create_subscription(Int32,"/arm_teleop/camAntena", self.callback2,10)
        self.subscriber_camAntena
        
        self.subscriber_servo_rotacion = self.create_subscription(Int32,"/arm_teleop/servo_rotacion", self.callback3,10)
        self.subscriber_servo_rotacion
        
    def limits(self,data, liminf,limsup):

        if data<liminf:
            data=liminf
        elif data>limsup:
            data=limsup
        return data
        
        
    def callback(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.camArm].angle = int(ndata)       
        except Exception as e:
            print(data.data)
            print(e)
            
            
    def callback2(self,data):
        try:
            ndata=self.limits(data.data,0,180)
            self.kit.servo[self.camAntena].angle = int(ndata)        
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
