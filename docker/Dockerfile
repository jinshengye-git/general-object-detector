FROM pytorch/pytorch:2.3.0-cuda12.1-cudnn8-runtime

# Arguments to take host's user UID and GID
ARG USER_ID
ARG GROUP_ID
ARG USERNAME

ARG UBUNTU_RELEASE_YEAR="22"
ARG CUDA_MAJOR="12"
ARG CUDA_MINOR="1"

ENV NVIDIA_DRIVER_CAPABILITIES \
    ${NVIDIA_DRIVER_CAPABILITIES:+$NVIDIA_DRIVER_CAPABILITIES,}compute,video,utility
ENV DEBIAN_FRONTEND=noninteractive

#RUN echo "Asia/Tokyo" > /etc/localtime ; echo "CUDA Version ${CUDA_MAJOR}.${CUDA_MINOR}.0" > /usr/local/cuda/version.txt

# Setup Locale
RUN apt-get update -y && apt-get install --no-install-recommends locales locales-all sudo
ENV LC_ALL en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US.UTF-8



RUN apt-get update -y && apt-get install --no-install-recommends software-properties-common lsb-release wget git git-lfs htop curl net-tools zsh zstd gawk tmux screen less udev build-essential cmake libboost-all-dev vim -y 
RUN apt-get install -y python3-pip python3-numpy python3-scipy python3-matplotlib openssh-client python3-setuptools libbluetooth-dev libeigen3-dev libarmadillo-dev libceres-dev libgoogle-glog-dev libgflags-dev libatlas-base-dev libsuitesparse-dev ffmpeg libgl1 libsm6 libxext6

RUN pip3 install opencv-python
RUN pip3 install pandas
RUN pip3 install ultralytics

RUN git clone https://github.com/jinshengye-git/general-object-detector.git

#USER ${USERNAME}
#RUN sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
#RUN curl -sLf https://spacevim.org/cn/install.sh | bash


