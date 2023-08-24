FROM osrf/ros:humble-desktop
LABEL maintainer="Ignacio Vizzo <ivizzo@uni-bonn.de>"

# Install utilities
RUN apt-get update && apt-get install --no-install-recommends -y \
    clang-format \
    clang-tidy \
    curl \
    git \
    rsync \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Install the Pylon SDK
RUN wget -nv https://www.baslerweb.com/fp-1682511100/media/downloads/software/pylon_software/pylon_7.3.0.27189_linux-x86_64_debs.tar.gz \
    && tar -xvf *.tar.gz \
    && apt-get install ./pylon_*.deb ./codemeter*.deb \
    && rm *.deb *.tar.gz

# Install Python3 utils
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache \
  anybadge \
  black \
  defusedxml \
  netifaces \
  numpy \
  pyautogui \
  rosnumpy \
  pylint \
  scipy

# Replace paramiko library with a fork that allow ssh conections with empty passwords
# For more details: https://github.com/paramiko/paramiko/issues/890
RUN python3 -m pip install --upgrade paramiko-ng

# install dependencies for the host machine. Mainly to speedup dev builds
RUN apt-get update && apt-get install --no-install-recommends -y \
    command-not-found \
    ethtool \
    htop \
    iproute2 \
    iputils-ping \
    net-tools \
    ruby-rubygems \
    silversearcher-ag \
    tmux \
    tree \
    vim \
    && rm -rf /var/lib/apt/lists/* \
    && gem install tmuxinator

# Add scripts used in most CI/CD configs
ADD ci_scripts/ /bin/

# Install ouster-ros dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-$ROS_DISTRO-pcl-ros \
    ros-$ROS_DISTRO-rviz2 \
    ros-$ROS_DISTRO-tf2-eigen \
    && rm -rf /var/lib/apt/lists/*

# Install ouster-ros dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    libcurl4-openssl-dev \
    libeigen3-dev \
    libjsoncpp-dev \
    libspdlog-dev \
    && rm -rf /var/lib/apt/lists/*

# Install pylon-ros dependencies
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-$ROS_DISTRO-diagnostic-updater \
    && rm -rf /var/lib/apt/lists/*

# Install Cyclone DDS
RUN apt-get update && apt-get install --no-install-recommends -y \
    ros-$ROS_DISTRO-rmw-cyclonedds-cpp \
    && rm -rf /var/lib/apt/lists/*

