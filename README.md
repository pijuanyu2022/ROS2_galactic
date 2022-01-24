# ROS2_galactic Tutorial

1, [ROS2_galactic Installtion](## 1, ROS2_galactic Installtion)
2, [I Publisher and Subscriber](### I Publisher and Subscriber)
3, [II Client and Service](### II Client and Service)
4, [IV Add msg and srv)(### IV Add msg and srv)

## 1, ROS2_galactic Installtion

Here is the tutorial from the ROS2 Documentation. http://docs.ros.org/en/galactic/Installation/Ubuntu-Install-Binary.html. I recommendate to run the ROS2 in linux environment. Right now, I am using Ubuntu 20.04 to run the ROS2 and the robot simulation. To install ubuntu 20.04 in your computer, please read this website and follow these instructions.https://ubuntu.com/download/desktop 

#### Step1: Add the ROS 2 apt repository. 

Use Ctrl+alt+T to open a new terminal window to Setup your sources.list. Then input 

    sudo apt install software-properties-common

    sudo add-apt-repository universe

    sudo apt update && sudo apt install curl gnupg lsb-release

    sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg

    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(source /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null

#### Step2: Downloading ROS 2. 

Go to this website https://github.com/ros2/ros2/releases/tag/release-galactic-20210716 and downlaod the ros2-galactic-20210616-linux-focal-amd64.tar.bz2 file. Then unpack it:

    mkdir -p ~/ros2_galactic

    cd ~/ros2_galactic

    tar xf ~/Downloads/ros2-galactic-20210616-linux-focal-amd64.tar.bz2

#### Step3: Installing and initializing rosdep

    sudo apt update

    sudo apt install -y python3-rosdep
    
    sudo rosdep init
    
    rosdep update

    rosdep install --from-paths ~/ros2_galactic/ros2-linux/share --ignore-src -y --skip-keys "cyclonedds fastcdr fastrtps rti-connext-dds-5.3.1 urdfdom_headers"

    sudo apt install -y libpython3-dev python3-pip

#### Step4: Environment setup

    . ~/ros2_galactic/ros2-linux/setup.bash

#### Step5: Test ROS2 Galactic

In one teriminal window
    . ~/ros2_galactic/ros2-linux/setup.bash

    ros2 run demo_nodes_cpp talker

In another terminal window
    . ~/ros2_galactic/ros2-linux/setup.bash
    
    ros2 run demo_nodes_py listener

## 2, ROS2_galactic tutorial
    
### I Publisher and Subscriber
#### Step1: Create a package:
    
    ros2 pkg create --build-type ament_python py_pubsub
    
#### Step2: write a publisher.py file:
    wget https://raw.githubusercontent.com/ros2/examples/master/rclpy/topics/minimal_publisher/examples_rclpy_minimal_publisher/publisher_member_function.py

#### Step3: write a subscriber.py file:

    wget https://raw.githubusercontent.com/ros2/examples/master/rclpy/topics/minimal_subscriber/examples_rclpy_minimal_subscriber/subscriber_member_function.py
    
#### Step4: add dependencies:
Open 'package.xml' with the text editor, fill 

    <description>Examples of minimal publisher/subscriber using rclpy</description>
    <maintainer email="pijuanyu2020@gmail">Pijuan Yu</maintainer>
    <license>Apache License 2.0</license>
    
After the lines above, add the following dependencies corresponding to your node’s import statements:

    <exec_depend>rclpy</exec_depend>
    <exec_depend>std_msgs</exec_depend>
    
#### Step5: Add an entry point:
Open the setup.py file. Match the maintainer:

    maintainer='Pijuan Yu',
    maintainer_email='pijuanyu2020@gmail.com',
    description='Examples of minimal publisher/subscriber using rclpy',
    license='Apache License 2.0',
    
Add the following line within the console_scripts brackets of the entry_points field:

    entry_points={
            'console_scripts': [
                    'minimal_publisher = py_pubsub.publisher_member_function:main',
                    'minimal_subscriber = py_pubsub.subscriber_member_function:main',
            ],
    },
   
Note: minimal_publisher and minimal_subscriber are used to launch the node, it is not the rostopic name and the node name

#### Step6: run the publisher node and subscriber node

    colcon build --packages-select py_pubsub
    
    . install/setup.bash
    
    ros2 run py_pubsub minimal_publisher
    
    ros2 run py_pubsub minimal_subscriber
    
    
### II Client and Service

#### Step1: Create a package

    ros2 pkg create --build-type ament_python py_srvcli --dependencies rclpy example_interfaces

example_interfaces is the package that includes the .srv file you will need to structure your requests and responses:

    int64 a
    int64 b
    ---
    int64 sum
  
#### Step2: Write the service_member_function.py and client_member_function.py
See the code in the package

#### Step3: Update pakcage.xml
Open package.xml:

    <description>This package is used to create a client and a service so that two intergers can be added</description>
    <maintainer email="pijuanyu2020@gmail">Pijuan Yu</maintainer>
    <license>Apache License 2.0</license>
    
#### Step4: Update setup.py
Open the setup.py file. Match the maintainer:

    maintainer='Pijuan Yu',
    maintainer_email='pijuanyu2020@gmail.com',
    description='This package is used to create a client and a service so that two intergers can be added',
    license='Apache License 2.0',
    
Add the following line within the console_scripts brackets of the entry_points field:

    entry_points={
            'console_scripts': [
                'service = py_service.service_member_function:main',
                'client = py_service.client_member_function:main',
            ],
    },

#### Step5: Build and Run

    colcon build
    
    . install/setup.bash
    
    ros2 run py_srvcli service
    
    ros2 run py_srvcli client 4 5
    
 
### IV Add msg and srv
 
#### Step1: create a new package

    ros2 pkg create --build-type ament_cmake tutorial_interfaces

In ros2_ws/src/tutorial_interfaces:
    
    mkdir msg
    
    mkdir srv

#### Step2: create custom files
In the tutorial_interfaces/msg directory:
    
    touch Num.msg
    
add these lines into the 'Num.msg' file
    
    int64 num
 
In the tutorial_interfaces/srv directory:

    touch AddThreeInts.srv

add these lines into the 'AddThreeInts.srv' file

    int64 a
    int64 b
    int64 c
    ---
    int64 sum

#### Step3: Update CMakeLists.txt
add these lines to 'CMakeLists.txt':

    find_package(rosidl_default_generators REQUIRED)

    rosidl_generate_interfaces(${PROJECT_NAME}
      "msg/Num.msg"
      "srv/AddThreeInts.srv"
    )
    
#### Step4: Update package.xml
add these lines to package.xml:

    <build_depend>rosidl_default_generators</build_depend>

    <exec_depend>rosidl_default_runtime</exec_depend>

    <member_of_group>rosidl_interface_packages</member_of_group>

#### Step5: Build and confirm

    colcon build
    
    . install/setup.bash
    
    ros2 interface show tutorial_interfaces/msg/Num
    
    ros2 interface show tutorial_interfaces/srv/AddThreeInts

#### Step6: Use the new interfaces
In the python file, add this line to use 

    from tutorial_interfaces.srv import AddThreeInts  
    
In the package.xml:
    <exec_depend>tutorial_interfaces</exec_depend>
    
    
    


    
