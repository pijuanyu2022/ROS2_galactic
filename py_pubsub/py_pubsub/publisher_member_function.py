# Copyright 2016 Open Source Robotics Foundation, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from threading import Timer
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalPublisher(Node):
    def __init__(self):
        super().__init__('minimal_publisher') # create node name
        self.publishers_ = self.create_publisher(String, 'publish_msg', 10) # create publisher, 'pub;ish_msg' is the rostopic name
        timer_period = 0.5 #seconds, it is a constant
        self.timer = self.create_timer(timer_period, self.timer_callback) # set a time call back
        self.i = 0

    def timer_callback(self):
        msg = String() # create a msg
        msg.data = 'Hello world: %d' % self.i # save the data into the msg
        self.publishers_.publish(msg) # publish the msg
        self.get_logger().info('Publising : "%s"' % msg.data) # equal to rospy.loginfo()
        self.i +=1

def main(args=None):
    rclpy.init(args=args) # initialize rclpy library
    minimal_publisher = MinimalPublisher() # create the node
    rclpy.spin(minimal_publisher) # spin the node

    minimal_publisher.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


    