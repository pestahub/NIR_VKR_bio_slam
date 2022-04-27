#!/usr/bin/python
#credits to: https://github.com/ros-teleop/teleop_twist_keyboard/blob/master/teleop_twist_keyboard.py

from __future__ import print_function
from hashlib import new
from math import sin, cos, pi

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

def y_from_quaternion(q):
  orientation_q = q.pose.pose.orientation
  orientation_list = [orientation_q.x, orientation_q.y, orientation_q.z, orientation_q.w]
  (r, p, y) = euler_from_quaternion (orientation_list)
  return y

def go_forwart(distance):
  start_odom = odom
  r = rospy.Rate(10)
  
  print(y_from_quaternion(odom), odom.pose.pose.position.x,start_odom.pose.pose.position.x, distance*cos(y_from_quaternion(odom)), )
  if (odom.pose.pose.position.x < start_odom.pose.pose.position.x + (distance*cos(y_from_quaternion(odom)))):
    while (odom.pose.pose.position.x < start_odom.pose.pose.position.x + (distance*cos(y_from_quaternion(odom)))):
      twist.linear.x = 0.4
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
      velocity_publisher.publish(twist)
      print(odom.pose.pose.position.x)
      r.sleep()
    return
  if (odom.pose.pose.position.x > start_odom.pose.pose.position.x + (distance*cos(y_from_quaternion(odom)))):
    while (odom.pose.pose.position.x > start_odom.pose.pose.position.x + (distance*cos(y_from_quaternion(odom)))):
      twist.linear.x = 0.4
      twist.linear.y = 0.0
      twist.linear.z = 0.0
      twist.angular.x = 0.0
      twist.angular.y = 0.0
      twist.angular.z = 0.0
      velocity_publisher.publish(twist)
      print(odom.pose.pose.position.x)
      r.sleep()
    return

def turn_left(angle):
  start_odom = odom
  r = rospy.Rate(10)
  start_yaw = y_from_quaternion(start_odom)
  start_yaw += pi
  start_yaw = start_yaw % 2*pi
  now_odom = y_from_quaternion(odom) + pi
  now_odom = now_odom % 2*pi
  new_angle = start_yaw + angle
  while now_odom > (new_angle+0.1) or now_odom < (new_angle-0.1):
    now_odom = y_from_quaternion(odom) + pi
    now_odom = now_odom % 2*pi
    print(start_yaw, now_odom, new_angle)
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = 0.4
    velocity_publisher.publish(twist)
    
    r.sleep()
  

def turn_right(angle):
  start_odom = odom
  r = rospy.Rate(10)
  new_angel = (y_from_quaternion(start_odom) - angle)
  if new_angel < 0: 
    new_angel*=-1
    new_angel = new_angel % pi
    new_angel *=-1
  else: 
    new_angel = new_angel % pi
  print(new_angel)
  while (y_from_quaternion(odom)) > (new_angel+0.05) or y_from_quaternion(odom) < (new_angel-0.05):

    print(y_from_quaternion(odom), y_from_quaternion(start_odom), angle)
    twist.linear.x = 0.0
    twist.linear.y = 0.0
    twist.linear.z = 0.0
    twist.angular.x = 0.0
    twist.angular.y = 0.0
    twist.angular.z = -0.4
    velocity_publisher.publish(twist)
    
    r.sleep()




def main():
  global velocity_publisher
  velocity_publisher = rospy.Publisher('cmd_vel', Twist, queue_size = 1)    
  joy_subscriber = rospy.Subscriber('odom/ground_truth', Odometry, odometry_callback)
  global twist
  twist = Twist()
  r = rospy.Rate(1)
  r.sleep()
  # turn_right(0.1)

  # go_forwart(7)
  # turn_left(3.1415)
  # go_forwart(7)
  turn_right(0.1)

  go_forwart(1)
  turn_left(pi/2)
  go_forwart(1)
  turn_left(pi/2)
  go_forwart(1)
  turn_left(pi/2)
  go_forwart(1)





if __name__ == "__main__":
    rospy.init_node('champ_teleop')
    main()