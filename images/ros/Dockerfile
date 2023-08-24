FROM osrf/ros:noetic-desktop-full
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
RUN wget -nv https://dnb-public-downloads-misc.s3.eu-central-1.amazonaws.com/pylon/pylon_6.2.0.21487-deb0_amd64.deb \
    && dpkg -i pylon*.deb \
    && rm pylon*.deb

# Install Python3 utils
RUN apt-get update && apt-get install --no-install-recommends -y \
    python3-pip \
    python3-tk \
    && rm -rf /var/lib/apt/lists/*

RUN python3 -m pip install --no-cache \
  anybadge \
  black \
  catkin-lint \
  catkin-tools \
  catkin_tools_fetch \
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
    ethtool \
    htop \
    iputils-ping \
    net-tools \
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
    libcurl4-openssl-dev \
    libeigen3-dev \
    libjsoncpp-dev \
    libspdlog-dev \
    && rm -rf /var/lib/apt/lists/*
