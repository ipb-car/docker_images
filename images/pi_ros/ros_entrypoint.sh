#!/bin/bash
sudo service ssh start
source "/home/pi-docker/catkin_ws/devel/setup.bash"
exec "$@"
