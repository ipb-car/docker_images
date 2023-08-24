cmake_minimum_required(VERSION 2.8.12)
project(rpi_time)

find_package(catkin REQUIRED)
find_package(message_generation REQUIRED)

catkin_package(CATKIN_DEPENDS)

install(
      PROGRAMS src/${PROJECT_NAME}.py
      DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}/scripts
)

