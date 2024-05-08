#!/bin/bash

xhost +

# nvidia-docker2
# docker run --runtime=nvidia --rm -it --env="DISPLAY" --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" kaibo_env_gui glxgears

# --env="QT_X11_NO_MITSHM=1" \ # prevent rviz menu turning black
USER_ID=$(id -u)
GROUP_ID=$(id -g)

#--runtime=nvidia -d \

docker run --rm --gpus all \
    --privileged \
    --network=host \
    --user=${USER_ID}:${GROUP_ID} \
    --name="general_obj_detect" \
    --env="NVIDIA_DRIVER_CAPABILITIES=all" \
    --env="QT_X11_NO_MITSHM=1" \
    --env="DISPLAY=$DISPLAY" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --env="XAUTHORITY=$XAUTH" \
    --volume="$XAUTH:$XAUTH" \
    --volume="$HOME/docker_share:/home/docker_share" \
    --volume="$HOME/datalogs:/home/datalogs" \
    --volume="$HOME/app:/src" \
    --volume="/dev:/dev" \
    general_obj_detect:latest \
    /bin/sh -c "while true; do sleep 10; done"

