# Intuitive_Control
Intuitive control of robotic arm using mixed reality

This are the Unity and Ros files developed to control the Franka Emika Panda using HTC vive.

Please install following packages into ROS library before the execution

1. ROS integration for Franka Emika research robots : https://github.com/frankaemika/franka_ros.git
2. panda_moveit_config package                      : https://github.com/ros-planning/panda_moveit_config.git
3. rosbridge_suite                                  : sudo apt-get install ros-<rosdistro>-rosbridge-server

Add the packages from this repository as well and compile your workspace.

To run the Unity Scene. Check the Input Bindings of the controller. Trigger should have a grabpinch click assigned and a custom action publish should be assigned as click to the gripper.

Run the rosbridge_websocket.launch from the package rosbridge_server
Run the demo.launch from the package panda_moveit_config
Run the new.py from the testing package. This program subscribes to pose array form unity intiallizes the the move group and verify the position of each of the waypoint and publish the results. Also, the cartesian path planning is done using this program.
