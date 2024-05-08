# Develop memo

Current stage just tested yolov5,  other functions not tested yet. also it is not supporting the streaming mode yet.

# Setup status:
0. `cd ~; mkdir docker_share; mkdir datalogs`
1. `./build.sh`
2. `./run.sh`
3.  open another terminal, and `cd general-object-detector/docker` then `./login.sh`

# Test
0. download [video.mp4](https://drive.google.com/file/d/1PNEoAyg5RLQP5ZUaPjFX-NTV4WzDkVrG/view?usp=drive_link) in your host PC $HOME/docker_share. 
1. login.sh script to access docker container's bash.
2. copy [video.mp4](https://drive.google.com/file/d/1PNEoAyg5RLQP5ZUaPjFX-NTV4WzDkVrG/view?usp=drive_link) to /workspace/general-object-detector/media/DrivingClips/ 
    `cp /home/docker_share/video.mp4 /workspace/general-object-detector/media/DrivingClips/`
3.  `cd /workspace/general-object-detector; python3 run.py --model yolov5s --f video -distances`