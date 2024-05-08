#!/bin/bash
#Sdocker system prune -a
# Get current user details
USER_ID=$(id -u)
GROUP_ID=$(id -g)
USERNAME=$(id -un)

echo $USERNAME
echo $USER_ID
echo $GROUP_ID

docker  build \
	--build-arg USER_ID=${USER_ID} \
  	--build-arg GROUP_ID=${GROUP_ID} \
  	--build-arg USERNAME=${USERNAME} \
	-t general_obj_detect .
