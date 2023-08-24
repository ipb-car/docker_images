FROM arm64v8/ros:humble-ros-base
# FROM ros:humble-ros-base
ENV USER_NAME="pi-docker"
ENV GROUP_ID=1000
ENV USER_ID=1000

# Install raspbian dependencies

RUN apt-get update && apt-get install --no-install-recommends -y \
    chrony \
    git \
    htop \
    pps-tools \
    python3-pip \
    ssh \
    vim \
    libboost-all-dev\
    && rm -rf /var/lib/apt/lists/*

# Add normal sudo-user to container, passwordless
RUN addgroup --gid $GROUP_ID $USER_NAME \
    && adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER_NAME \
    && adduser $USER_NAME dialout \
    && adduser $USER_NAME sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && sed -i 's/required/sufficient/' /etc/pam.d/chsh \
    && touch /home/$USER_NAME/.sudo_as_admin_successful

# Enable passwordlews access to this docker container from outside + change default ssh port to
# simplify the setuo on the rpi(which has port 22 by default). You can still skip this step, ssh
# into the container, but won't be able to run ros remotely (bridge network will be a different net
# than the one from the roscore)
RUN passwd -d $USER_NAME \
    && sed -i -Ee 's/^#?[[:blank:]]*PermitEmptyPasswords[[:blank:]]*no[[:blank:]]*$/PermitEmptyPasswords yes/' /etc/ssh/sshd_config \
    && sed -i -Ee 's/^#?[[:blank:]]*Port[[:blank:]]*22[[:blank:]]*$/Port 2222/' /etc/ssh/sshd_config

# Switch to local user and bootstrap the dev installation
USER $USER_NAME

# # Clone and build ROS custom packages
SHELL ["/bin/bash", "-c"]
RUN mkdir -p /home/$USER_NAME/catkin_ws/src/
WORKDIR /home/$USER_NAME/colcon_ws/src
WORKDIR /home/$USER_NAME/colcon_ws/src/sbg_ros2_driver
RUN rosdep update

RUN git clone --depth 1 https://github.com/SBG-Systems/sbg_ros2_driver.git \
    && rosdep install --from-path /home/$USER_NAME/colcon_ws/src/sbg_ros2_driver \
    && cd /home/$USER_NAME/colcon_ws \
    && source /opt/ros/humble/setup.bash && colcon build \
    && source install/setup.bash

COPY rpi_time /home/$USER_NAME/colcon_ws/src/rpi_time 
WORKDIR /home/$USER_NAME/colcon_ws
RUN colcon build && source install/setup.bash

# setup entrypoint, inspired in the osrf docker images but using our custom login profile
COPY ./env.sh /opt/ros/humble/
# COPY ./env.sh /home/$USER_NAME/colcon_ws/devel/
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash", "--login"]
