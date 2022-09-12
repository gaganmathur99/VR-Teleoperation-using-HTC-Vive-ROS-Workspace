#!/usr/bin/env python
"""
    Subscribes to SourceDestination topic.
    Uses MoveIt to compute a trajectory from the target to the destination.
    Trajectory is then published to PickAndPlaceTrajectory topic.
"""
import rospy

from project_msg.msg import FrankaJoints


def callback(msg):
    rospy.loginfo(rospy.get_caller_id() + "I heard:\n%s", msg.joints)
    joint_.joints = msg.joints
    rospy.loginfo(rospy.get_caller_id() + "I talk:\n%s", joint_.joints)
    pub.publish(joint_)
    rospy.Rate(2) 


if __name__ == '__main__':
    rospy.init_node('Trajectory_Subscriber', anonymous=True)
    sub = rospy.Subscriber("/Franka_Joints", FrankaJoints, callback)
    pub = rospy.Publisher("/franka_robot_joint_transfer", FrankaJoints)
    joint_ = FrankaJoints()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()