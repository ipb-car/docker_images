#!/bin/bash
export ROS_MASTER_URI=http://192.168.1.100:11311
export ROS_IP=192.168.1.100
export ROSLAUNCH_SSH_UNKNOWN=1
export HISTFILE=$HOME/ros_ws/.bash_history
source /opt/ros/$ROS_DISTRO/setup.bash 2>/dev/null || true
source $HOME/ros_ws/devel/setup.bash 2>/dev/null || true
