#!/usr/bin/env python
"""
    Subscribes to SourceDestination topic.
    Uses MoveIt to compute a trajectory from the target to the destination.
    Trajectory is then published to PickAndPlaceTrajectory topic.
"""
import rospy

from sensor_msgs.msg import JointState
from project_msg.msg import FrankaJoints

def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard:\n%s", msg.position)
    joint_.joints = msg.position[:7]
    rospy.loginfo(rospy.get_caller_id() + "I talk:\n%s", joint_.joints)
    pub.publish(joint_)
    rospy.Rate(20) 


if __name__ == '__main__':
    rospy.init_node('franka_state_feedback', anonymous=True)
    sub = rospy.Subscriber("/joint_states", JointState, callback)
    pub = rospy.Publisher("/franka_robot_joint_transfer", FrankaJoints)
    joint_ = FrankaJoints()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()