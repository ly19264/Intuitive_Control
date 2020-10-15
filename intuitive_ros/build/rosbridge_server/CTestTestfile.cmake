# CMake generated Testfile for 
# Source directory: /home/nitish/intuitive_ros/src/rosbridge_suite/rosbridge_server
# Build directory: /home/nitish/intuitive_ros/build/rosbridge_server
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(_ctest_rosbridge_server_rostest_test_websocket_test_smoke.test "/home/nitish/intuitive_ros/build/rosbridge_server/catkin_generated/env_cached.sh" "/usr/bin/python2" "/opt/ros/melodic/share/catkin/cmake/test/run_tests.py" "/home/nitish/intuitive_ros/build/rosbridge_server/test_results/rosbridge_server/rostest-test_websocket_test_smoke.xml" "--return-code" "/usr/bin/python2 /opt/ros/melodic/share/rostest/cmake/../../../bin/rostest --pkgdir=/home/nitish/intuitive_ros/src/rosbridge_suite/rosbridge_server --package=rosbridge_server --results-filename test_websocket_test_smoke.xml --results-base-dir \"/home/nitish/intuitive_ros/build/rosbridge_server/test_results\" /home/nitish/intuitive_ros/src/rosbridge_suite/rosbridge_server/test/websocket/test_smoke.test ")
subdirs("gtest")
