#!/usr/bin/env python
"""
    Subscribes to SourceDestination topic.
    Uses MoveIt to compute a trajectory from the target to the destination.
    Trajectory is then published to PickAndPlaceTrajectory topic.
"""
import rospy

#from frankaunity.msg import FrankaMoveitJoints
from geometry_msgs.msg import PoseStamped

def callback(data):
    rospy.loginfo(rospy.get_caller_id() + "I heard:\n%s", data)
    target_pose = data
    rospy.loginfo(rospy.get_caller_id() + "I talk:\n%s", target_pose)
    pub.publish(target_pose)
    rospy.Rate(2) 


if __name__ == '__main__':
    rospy.init_node('Trajectory_Subscriber', anonymous=True)
    sub = rospy.Subscriber("/target_pose",PoseStamped, callback)
    pub = rospy.Publisher("/cartesian_impedance_example_controller/equilibrium_pose", PoseStamped)
    target_pose = PoseStamped()
    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()