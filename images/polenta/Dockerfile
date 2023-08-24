# Base image with almost everything but ROS installed
FROM prbonn/ros:noetic
LABEL maintainer="Ignacio Vizzo <ivizzo@uni-bonn.de>"
ENV USER_NAME="ipb_car"
ARG GROUP_ID=1000
ARG USER_ID=1000
ENV TERM=xterm-256color

# Add custom configuration files to docker containter
COPY etc /etc/

# setup entrypoint, inspired in the osrf docker images but using our custom login profile
COPY ./ros_entrypoint.sh /

# Add normal sudo-user to container, passwordless
RUN addgroup --gid $GROUP_ID $USER_NAME \
    && adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER_NAME \
    && adduser $USER_NAME sudo \
    && echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers \
    && sed -i 's/required/sufficient/' /etc/pam.d/chsh \
    && touch /home/$USER_NAME/.sudo_as_admin_successful

# Switch to local user and setup entry points
USER $USER_NAME

# Need this file for the python monitor
RUN touch /home/$USER_NAME/.Xauthority

# Setup workdir and entrypoint
WORKDIR /home/$USER_NAME/ros_ws
ENTRYPOINT ["/ros_entrypoint.sh"]
CMD ["bash", "--login"]
