#!/bin/bash
sudo service ssh start
source "/home/pi-docker/colcon_ws/install/setup.bash"
exec "$@"
