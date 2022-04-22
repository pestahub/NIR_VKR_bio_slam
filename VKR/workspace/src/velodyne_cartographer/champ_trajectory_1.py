#!/usr/bin/python
#credits to: https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py

from __future__ import print_function

import roslib; roslib.load_manifest('champ_teleop')
import rospy

from sensor_msgs.msg import Joy
from geometry_msgs.msg import Twist
from champ_msgs.msg import Pose as PoseLite
from geometry_msgs.msg import Pose as Pose
import tf

import sys, select, termios, tty
import numpy as np


def main():
  velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 1)    
  twist = Twist()
  r = rospy.Rate(10) # 10hz 
  r.sleep()
  now = rospy.get_rostime()

  while not rospy.is_shutdown():
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    
    print (now.secs, rospy.Time.now().secs)
    if (now.secs < rospy.Time.now().secs - 1):
     
      twist.linear.x = 0.0
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = -0.1

    if (now.secs < rospy.Time.now().secs - 2):
      
      twist.linear.x = 0.4
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
    if (now.secs < rospy.Time.now().secs - 15):
      
      twist.linear.x = 0.0
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.3
    if (now.secs < rospy.Time.now().secs - 22):

      
      twist.linear.x = 0.4
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
    if (now.secs < rospy.Time.now().secs - 40):

      
      twist.linear.x = 0.0
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
    velocity_publisher.publish(twist)
    r.sleep()

   

if __name__ == "__main__":
    rospy.init_node('champ_teleop')
    main()