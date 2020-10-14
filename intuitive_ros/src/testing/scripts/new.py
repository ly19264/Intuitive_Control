#!/usr/bin/python
import sys
import copy
import rospy
import moveit_commander
import moveit_msgs.msg
import geometry_msgs.msg
from math import pi
from std_msgs.msg import String
from moveit_commander.conversions import pose_to_list
from geometry_msgs.msg import Pose
from geometry_msgs.msg import PoseArray

from testing.msg import array


def listener():
    moveit_commander.roscpp_initialize(sys.argv)
    rospy.init_node('move_arm_panda',anonymous=True)
    #Receive the Pose Array
    #print("Start of Reception")
    msg = rospy.wait_for_message('/posearray', PoseArray)
    #print(msg)
    return (msg)

def intialize():

    robot = moveit_commander.RobotCommander()
    scene = moveit_commander.PlanningSceneInterface()
    group_name = "panda_arm"
    group = moveit_commander.MoveGroupCommander(group_name) 
    display_trajectory_publisher = rospy.Publisher('/display_planned_path',moveit_msgs.msg.DisplayTrajectory,queue_size=20)
    return group,robot

def robot_arm_state(group,robot):
    planning_frame = group.get_planning_frame()
    #print "============ Reference frame: %s" % planning_frame
    # We can also print the name of the end-effector link for this group:
    eef_link = group.get_end_effector_link()
    #print "============ End effector: %s" % eef_link

    # We can get a list of all the groups in the robot:
    group_names = robot.get_group_names()
    #print "============ Robot Groups:", robot.get_group_names()

    # Sometimes for debugging it is useful to print the entire state of the
    # robot:
    #print "============ Printing robot state"
    #print type(robot.get_current_state())
    #print ""

def move_plan(group,goal_pose):
    #Generate the plan for each waypoint
    group.set_pose_target(goal_pose)  
    plan = group.plan()
    return plan

def WayCheckPublisher(waycheckres):
    simple_publisher = rospy.Publisher('WayCheck', array, queue_size = 10)
    #rospy.init_node('WayCheck_1', anonymous=False)
    rate = rospy.Rate(1)

    waycheck = array()

    waycheck.int_array = waycheckres

    #while not rospy.is_shutdown():
    for i in range (30):
        simple_publisher.publish(waycheck) # Desired topic publishes
        rate.sleep()   # Insures the topic is published at the required frequency.
    
    return

if __name__ == '__main__':
    array_pose = listener()         #Get the Pose Array
    (group,robot) = intialize()     #Initialize the robot controllers
    robot_arm_state(group,robot)    #Get the robot State... Mostly for Debugging
    all_good = 0                    #All the Waypoints are in the Reachable Workspace of the arma
    waypoint_count = len(array_pose.poses)  #Get the No. of waypoints set 
    waypoint_check = []                     #To get the waypoint which might be out of bounds
    for x in range(waypoint_count):
        pose_data = array_pose.poses[x]     #Getting individual Poses from the Pose Array
        plan = move_plan(group,pose_data)   #Plan a trajectory to the waypoint to check the workspace limits     
        if not plan.joint_trajectory.points:
            waypoint_check.insert(x, 1)     #Waypoint is out of reach
            all_good = 1                    #Stop the cartesian planning
            print("Plan Failed !!!!!!")
        else:
            waypoint_check.insert(x, 2)     #Waypoint is in reach

    #count = len(waypoint_check)

    WayCheckPublisher(waypoint_check)       #Publish the result of waypoint check

    if all_good == 0:
        (plan, fraction) = group.compute_cartesian_path(
                                       array_pose.poses,   # waypoints to follow
                                       0.01,        # eef_step
                                       0.0)         # jump_threshold
        group.execute(plan,wait=True)
    else:
        print "Planning Failed. Some waypoint out of bound"
    #test = plan.joint_trajectory.points[0] 
    #print test.positions
    #print group.get_current_pose().pose
    print waypoint_check
    #robot_arm_state(group,robot)    #Get the robot State... Mostly for Debugging   
