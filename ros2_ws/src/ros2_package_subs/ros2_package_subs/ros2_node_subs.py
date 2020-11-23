import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist

class Subs(Node):
    def __init__(self):
        super().__init__('ros2_package_subs')
        self.subscription = self.create_subscription(
            Twist,
            'turtle1/cmd_vel',
            self.listener_callback,
            1)
        self.subscription
    def listener_callback(self, msg):
        lX = str(msg.linear.x)
        lY = str(msg.linear.y)
        lZ = str(msg.linear.z)
        aX = str(msg.angular.x)
        aY = str(msg.angular.y)
        aZ = str(msg.angular.z)
        result = "\nLinear: \n \tx = {0}\n \ty = {1}\n \tz = {2} \nAngular: \n \tx = {3}\n \ty = {4} \n \tz = {5}\n".format(lX, lY, lZ, aX, aY, aZ)
        self.get_logger().info(result)
        
        
def main(args=None):
    rclpy.init(args=args)
    subs = Subs()
    rclpy.spin(subs)
    subs.destroy_node()
    rclpy.shutdown()


if __name__ == '__main__':
    main()
