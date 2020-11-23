#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist

def talker():
	pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
	rospy.init_node('ros1_talker_turtle')
	rate = rospy.Rate(1) #1hz
	vel_msg = Twist()
	
	#Definindo os valores de movimentação da tartaruga
	vel_msg.linear.x = 2.0
	vel_msg.linear.y = 0.0
	vel_msg.linear.z = 0.0
	vel_msg.angular.x = 0.0
	vel_msg.angular.y = 0.0
	vel_msg.angular.z = 1.8

	while not rospy.is_shutdown():
		rospy.loginfo(vel_msg)
		pub.publish(vel_msg)
		rate.sleep()

if __name__ == '__main__':
	try:
		talker()
	except rospy.ROSInterruptException:
		pass
