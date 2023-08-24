#!/bin/bash
set -e

# setup ros environment
. /etc/profile.d/ros_setup.sh
exec "$@"
