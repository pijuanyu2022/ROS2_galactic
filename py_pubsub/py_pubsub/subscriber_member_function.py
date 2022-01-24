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

import rclpy
from rclpy.node import Node
from std_msgs.msg import String

class MinimalSubscriber(Node):

    def __init__(self):
        super().__init__('minimal_subscriber') # create node name
        self.subscription = self.create_subscription(String, 'publish_msg', self.callback, 10) # create subscriber, 'publish_msg' is the subscriber rostopic
        self.subscription # prevent unused variable warning

    def callback(self, msg):
        self.get_logger().info('I heard: %s' %msg.data)

def main(args=None):
    rclpy.init(args=args) # initialize rclpy library
    
    minimal_subscriber = MinimalSubscriber() # create the node

    rclpy.spin(minimal_subscriber) # spin the node
    minimal_subscriber.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()


    