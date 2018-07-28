#!/usr/bin/env python
# license removed for brevity
import rospy
import os , sys, select, termios, tty
import math
#import Tkinter as tk
from sensor_msgs.msg import JointState
from std_msgs.msg import Float64
from geometry_msgs.msg import Twist
from math import pi

pub = rospy.Publisher('/joint_states', JointState, queue_size=10)
my_msg = JointState()
	
def mypublisher():


    rospy.init_node('teleop', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    
    my_msg.name=['right_front_wheel_joint','right_back_wheel_joint','left_front_wheel_joint','left_back_wheel_joint']
    my_msg.position = [0,0,0,0]
    i=0#the position of all four wheels
    jr1=0#position of base_to_right_arm_1
    jr2=0#position of joint_of_right_arm
    jl1=0#position of base_to_left_arm_1
    jl2=0#position of joint_of_left_arm
    i_1=0
    while not rospy.is_shutdown():

        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        old_settings[3] = old_settings[3] & ~termios.ICANON & ~termios.ECHO
        try :
            tty.setraw( fd )
            ch = sys.stdin.read( 1 )
        finally :
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
 
        my_msg.header.seq = i_1
        my_msg.header.stamp = rospy.Time.now() 
  	#my_msg.position = [i*0.0314,0,0,0,0,0,0,0]
        ##my_msg.velocity = [i,i,i,i,i,i,i,i]
	if ch == 'w':
                i=i+0.2
		my_msg.position= [i,i,i,i]
        elif ch =='e':
                i=i-0.2
                my_msg.position= [i,i,i,i]
	
	elif ch == 'q':
		exit()
 
        i_1 = i_1 + 1
	rospy.loginfo(my_msg)
        pub.publish(my_msg)
        

        rate.sleep()

	stop_robot();

def stop_robot():
    #cmd.linear.x = 0.0
   # cmd.angular.z = 0.0
    pub.publish(my_msg)


if __name__ == '__main__':
    try:
        mypublisher()
    except rospy.ROSInterruptException:
        pass
