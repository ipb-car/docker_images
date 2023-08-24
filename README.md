# ipb-car docker image

A simple image to support the CI/CD build on our gitlab server

## How to use

Just add a `Dockerfile` inside the [images](images/) folder, for example:

```sh
images/ros_melodic/Dockerfile
```

Inside each folder you should define how to build your docker container, the CI/CD will
automagically create dynamically the jobs on the fly for you, so no need to touch it
