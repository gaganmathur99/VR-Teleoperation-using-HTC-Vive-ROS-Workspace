#!/usr/bin/env python

import random
import rospy
import rosgraph
import time
from http import client
from pydoc import cli
import actionlib
from std_msgs.msg import String
from unity_robotics_demo_msgs.msg import HandCmd
from franka_gripper.msg import MoveAction, MoveGoal
from franka_gripper.msg import GraspAction, GraspGoal


TOPIC_NAME = 'Hand_Gesture'
NODE_NAME = 'Hand_Command_Subscriber'

def callback(data):
    cmd = data.data
    if (cmd == "Open_Gripper"):
        try:
            result_open = open_gripper()
            print ("Open Gripper result: ",result_open)
        except rospy.ROSInterruptException as e:
            print ('something went wrong',e)
    elif (cmd == "Grasp"):
        try:
            result_grasp = grasp()
            print ("Grasp Gripper result: ",result_grasp)
        except rospy.ROSInterruptException as e:
            print ('something went wrong',e)

#Action client to open the gripper fingers 
def open_gripper():

    client = actionlib.SimpleActionClient('/franka_gripper/move',MoveAction)
    client.wait_for_server()

    msg = MoveGoal()
    msg.width = 0.08
    msg.speed = 1
    client.send_goal_and_wait(msg)
    rospy.Rate(10) 
    client.wait_for_result()
    results = client.get_result()
    return results

#Action client to grasp an object
def grasp():

    
    client = actionlib.SimpleActionClient('/franka_gripper/grasp',GraspAction)
    client.wait_for_server()

    msg = GraspGoal()
    msg.width = 0.03
    msg.epsilon.inner = 0.005
    msg.epsilon.outer = 0.005
    msg.force = 5
    msg.speed = .08
    client.send_goal_and_wait(msg)
    rospy.Rate(10) 
    client.wait_for_result()
    results = client.get_result()
    return results

def feedback_move(msg):
    print("Move feedback: ",msg)


def feedback_grasp(msg):
    print("Grasp feedback: ",msg)


if __name__ == '__main__':#
    try:
        rospy.init_node(NODE_NAME, anonymous=True)
        rospy.Subscriber(TOPIC_NAME, String, callback)
        rospy.spin()
    except rospy.ROSInterruptException as e:
        print ('something went wrong',e)


   
