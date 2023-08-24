# ipb-car docker image for raspberry pi

This branch build a docker image with ubuntu and ROS to run in the raspberry pi and pushs it to docker hub.

The docker image used in the CI to build has installed `dockerx` to be able to build the image for `arm`.

The steps to build the docker image are:
* Install `cmake 3.20` (the default ubuntu version fails, see [here](https://gitlab.ipb.uni-bonn.de/ipb-team/robots/ipb-car/raspberry/pi-gen/-/issues/23))
* Install dependencies
* Install python3 pip packages
* Install ROS
* Build custom ROS packages
* Setup entrypoint
* Add authorized keys and permit root login.

# Integration with raspbian image

After building the image, it's pushed to docker hub relying on the CI variables `CI_REGISTRY_IMAGE_RPI` and `CI_REGISTRY_PASSWORD_RPI`, which contain the username and password of the dockerhub account.

This image is downloaded in the building process of the [raspbian image](https://gitlab.ipb.uni-bonn.de/ipb-team/robots/ipb-car/raspberry/pi-gen/-/tree/master/) and will be run as soon as the raspberry pi starts. Everything ROS-related happens here while the network configuration and devices setup is done in the raspbian image.

# Debugging

We can ssh to the running docker container but running `ssh root@pi` from polenta.

Alternatively, we can ssh to the raspberry pi via `ssh pi@pi -p 2244` and then run `docker exec -it docker_pi /bin/bash`, which will open a terminal inside the running docker container.

