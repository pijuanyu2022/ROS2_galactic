import rclpy
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MinimalService(Node):

    def __init__(self):
        super().__init__('minimal_service') # 'minimal_service' is the node name
        self.srv = self.create_service(AddTwoInts, 'add_two_ints', self.callback) #'add_two_ints is the rostopic name

    def callback(self, request, response):
        response.sum = request.a + request.b # add two integetrs
        self.get_logger().info('Incoming request\na: %d b: %d' %(request.a, request.b)) #\n is to go to the second line
        
        return response
    
def main(args=None):
    rclpy.init(args=args)
    minimal_service = MinimalService()
    rclpy.spin(minimal_service)

    minimal_service.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    