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
from franka_gripper.msg import GraspAction, GraspGoal


TOPIC_NAME = 'Hand_Gesture'
NODE_NAME = 'Hand_Command_Grasp_Subscriber'

def callback(data):
    cmd = data.data
    if (cmd == "Grasp"):
        try:
            grasp()
            print("Closing Gripper")
        except rospy.ROSInterruptException as e:
            print ('something went wrong',e)


#Action client to grasp an object
def grasp():
    
    client = actionlib.SimpleActionClient('/franka_gripper/grasp',GraspAction)
    client.wait_for_server()
    print("Closing Gripper Action")

    msg = GraspGoal()
    msg.width = 0.03
    msg.epsilon.inner = 0.005
    msg.epsilon.outer = 0.005
    msg.force = 5
    msg.speed = 0.1
    client.send_goal(msg)
    client.wait_for_result()
    results_grasp = client.get_result()
    return results_grasp

if __name__ == '__main__':
    try:
        rospy.init_node(NODE_NAME, anonymous=True)
        rospy.Subscriber(TOPIC_NAME, String, callback)
        rospy.spin()
    except rospy.ROSInterruptException as e:
        print ('something went wrong',e)


   
