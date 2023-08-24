FROM arm64v8/ros:noetic-robot
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
    && rm -rf /var/lib/apt/lists/*

# Install ROS dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-noetic-geometry \
    ros-noetic-geometry-msgs \
    ros-noetic-message-generation \
    ros-noetic-nmea-navsat-driver \
    ros-noetic-tf2 \
    ros-noetic-tf2-geometry-msgs \
    ros-noetic-tf2-msgs \
    ros-noetic-tf2-ros \
    && rm -rf /var/lib/apt/lists/*

# install cakin tools
RUN pip install catkin-tools

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

# Clone and build ROS custom packages
WORKDIR /home/$USER_NAME/catkin_ws/
RUN mkdir -p /home/$USER_NAME/catkin_ws/src/
COPY rpi_time /home/$USER_NAME/catkin_ws/src/rpi_time
RUN git clone --depth 1 https://github.com/SBG-Systems/sbg_ros_driver.git /home/$USER_NAME/catkin_ws/src/sbg_ros_driver
RUN . /opt/ros/noetic/setup.sh catkin config --extend /opt/ros/noetic && catkin build

# setup entrypoint, inspired in the osrf docker images but using our custom login profile
COPY ./env.sh /opt/ros/noetic/
COPY ./env.sh /home/$USER_NAME/catkin_ws/devel/
COPY ./ros_entrypoint.sh /

ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash", "--login"]
