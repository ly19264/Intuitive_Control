#!/usr/bin/python
import sys
import copy
import rospy
import time

from testing.msg import array

def WayCheckPublisher(waycheckres):
    simple_publisher = rospy.Publisher('WayCheck', array, queue_size = 10)
    rospy.init_node('WayCheck_1', anonymous=False)
    rate = rospy.Rate(1)

    waycheck = array()

    waycheck.int_array = waycheckres

    #waycheck = Int16MultiArray()
    #waycheck = waycheckres

    while not rospy.is_shutdown():
        simple_publisher.publish(waycheck) # Desired topic publishes
        rate.sleep()   # Insures the topic is published at the required frequency.
    
    return

if __name__ == '__main__':

    waypoint_check = []
    waypoint_check.insert(1, 1)
    waypoint_check.insert(2, 0)
    waypoint_check.insert(3, 1)
    waypoint_check.insert(4, 0)
    print "Start of Delay"
    time.sleep(5)
    print "End of Delay"
    WayCheckPublisher(waypoint_check)
