## ROS2_galactic

### ROS Installtion

Here is the tutorial from the ROS2 Documentation. http://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Binary.html. I recommendate to run the ROS2 in linux environment. Right now, I am using Ubuntu 20.04 to run the ROS2 and the robot simulation. To install ubuntu 20.04 in your computer, please read this website and follow these instructions.https://ubuntu.com/download/desktop 

#### Ubuntu install of ROS2 Galactic

Step1: Add the ROS 2 apt repository. 

Use Ctrl+alt+T to open a new terminal window to Setup your sources.list. Then input 

    sudo apt install software-properties-common

    sudo add-apt-repository universe

    sudo apt update && sudo apt install curl gnupg lsb-release

    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

Step2: Downloading ROS 2. 

Go to this website https://github.com/ros2/ros2/releases/tag/release-galactic-20210716 and downlaod the ros2-galactic-20210616-linux-focal-amd64.tar.bz2 file. Then unpack it:

    mkdir -p ~/ros2_galactic

    cd ~/ros2_galactic

    tar xf ~/Downloads/ros2-galactic-20210616-linux-focal-amd64.tar.bz2

Step3: Installing and initializing rosdep

    sudo apt update

    sudo apt install -y python3-rosdep
    
    sudo rosdep init
    
    rosdep update

    rosdep install --from-paths ~/ros2_galactic/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps rti-connext-dds-5.3.1 urdfdom_headers"

    sudo apt install -y libpython3-dev python3-pip

Step4: Environment setup

    . ~/ros2_galactic/ros2-linux/setup.bash

Step5: Test ROS2 Galactic

In one teriminal window
    . ~/ros2_galactic/ros2-linux/setup.bash

    ros2 run demo_nodes_cpp talker

In another terminal window
    . ~/ros2_galactic/ros2-linux/setup.bash
    
    ros2 run demo_nodes_py listener
