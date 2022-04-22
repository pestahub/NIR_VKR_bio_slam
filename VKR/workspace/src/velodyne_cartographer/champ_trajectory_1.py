#!/usr/bin/python
#credits to: https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py

from __future__ import print_function

import roslib; roslib.load_manifest('champ_teleop')
import rospy

from sensor_msgs.msg import Joy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import Twist
from champ_msgs.msg import Pose as PoseLite
from geometry_msgs.msg import Pose as Pose
import tf

import sys, select, termios, tty
import numpy as np
from tf.transformations import euler_from_quaternion, quaternion_from_euler


def odometry_callback(data):
  global odom
  odom = data

def turn_back(odom_now, start_turn_pose):
  orientation_q = odom_now.pose.pose.orientation
  orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
  (roll_now, pitch_now, yaw_now) = euler_from_quaternion (orientation_list)
  orientation_s = start_turn_pose.pose.pose.orientation
  orientation_list = [orientation_s.x, orientation_s.y, orientation_s.z, orientation_s.w]
  (roll_start, pitch_start, yaw_start) = euler_from_quaternion (orientation_list)
  
  if (yaw_now > yaw_start + 3.1415):
    return True
  else:
    return False




def main():
  velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 1)    
  joy_subscriber = rospy.Subscriber('odom/ground_truth', Odometry, odometry_callback)
  twist = Twist()
  r = rospy.Rate(10) # 10hz 
  r.sleep()
  now = rospy.get_rostime()
  start_odom = odom
  start_turn_pose = odom
  stage = 0
  while not rospy.is_shutdown():
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.0
    
    print (now.secs, rospy.Time.now().secs)
    
    if ((now.secs < rospy.Time.now().secs - 1) and (stage < 2)):
      stage = 1
     
      twist.linear.x = 0.0
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = -0.1

    if (now.secs < rospy.Time.now().secs - 2) and stage < 3:
      stage = 2
      twist.linear.x = 0.4
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
      start_turn_pose = odom
    if (odom.pose.pose.position.x > start_odom.pose.pose.position.x + 7) and stage < 4:
      stage = 3
      twist.linear.x = 0.0
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.3
      
    if (turn_back(odom, start_turn_pose)) and stage < 5:
      stage = 4
      
      
      twist.linear.x = 0.4
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
    if (odom.pose.pose.position.x < start_odom.pose.pose.position.x) and stage > 3:

      start_turn_pose = odom
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