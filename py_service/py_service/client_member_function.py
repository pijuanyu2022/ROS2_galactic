import rclpy
import sys
from rclpy.node import Node
from example_interfaces.srv import AddTwoInts

class MinimalClient(Node):

    def __init__(self):
        super().__init__('minimal_client') # 'minimal_service' is the node name
        self.client = self.create_client(AddTwoInts, 'add_two_ints') # create client, the type and the name must match the service
        while not self.client.wait_for_service(timeout_sec=1.0): # wait for 1 second
            self.get_logger().info('service not available, waiting again....')

        self.req = AddTwoInts.Request()

    def send_request(self):
        self.req.a = int(sys.argv[1]) # request sys number
        self.req.b = int(sys.argv[2])
        self.future = self.client.call_async(self.req) # call the request
    
def main(args=None):
    rclpy.init(args=args)

    minimal_client = MinimalClient()
    minimal_client.send_request() # send the request

    while rclpy.ok(): # if the name and type of client match these of service
        rclpy.spin_once(minimal_client) # spin once to request the number
        if minimal_client.future.done(): # if get two number
            try:
                response = minimal_client.future.result() # output result 
            except Exception as e:
                minimal_client.get_logger().info('Service call failed %r' %(e,)) # failed to get the number
            else:
                minimal_client.get_logger().info('Result of add_two_ints: for %d + %d = %d'%( # print the sum of two intergers
                    minimal_client.req.a, minimal_client.req.b, response.sum))    
            break

    minimal_client.destroy_node()
    rclpy.shutdown()

if __name__ == '__main__':
    main()
    