#!/usr/bin/env python
import rospy

#import the message type as per the reqirement to publish.
from std_msgs.msg import String
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray

# publisher object function : rospy.Publisher
# rospy.Publisher has arguments , topic name , topic type and queue_size
# rospy.init_node intializes the node and has the arguments node name and 
# rospy.Rate defines the rate at which the information is published to the topic. The argument is in hertz.


def simplePublisher():
    simple_publisher = rospy.Publisher('PoseArray', PoseArray, queue_size = 10)
    rospy.init_node('PoseArray_1', anonymous=False)
    rate = rospy.Rate(1)

    # The string to be published on the topic

    ps = PoseArray()
    pose = Pose()
    pose.position.x = 0.2
    pose.position.y = 0.2
    pose.position.z = 0.2
    pose.orientation.x = 0
    pose.orientation.y = 0
    pose.orientation.z = 1
    pose.orientation.w = 1
    ps.poses.append(pose)

    pose = Pose()
    pose.position.x = 0.4
    pose.position.y = 0.4
    pose.position.z = 0.4
    pose.orientation.x = 0
    pose.orientation.y = 0
    pose.orientation.z = 0
    pose.orientation.w = 1
    ps.poses.append(pose)

    pose = Pose()
    pose.position.x = 0.1
    pose.position.y = 0.1
    pose.position.z = 0.8
    pose.orientation.x = 0
    pose.orientation.y = 0
    pose.orientation.z = 0
    pose.orientation.w = 1
    ps.poses.append(pose)
    

    while not rospy.is_shutdown():
        simple_publisher.publish(ps) # Desired topic publishes
        rate.sleep()   # Insures the topic is published at the required frequency.

if __name__ == '__main__':
    try:
        simplePublisher()	
    except rospy.ROSInterruptException:
        pass
