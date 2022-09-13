#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

from std_msgs.msg import Float32

import random


class SousVide(Node):
    def __init__(self, node_name: str, **kwargs):
        super().__init__(node_name)
        self.pub_temp = self.create_publisher(Float32, "temperature", 1)

        self.get_logger().info("Started SousVide node.")
        self.run()

    def run(self):
        msg = Float32()
        msg.data = 10 + 60 * random.random()
        self.pub_temp.publish(msg)


def main(args=None):
    rclpy.init(args=args)

    node = SousVide("sous_vide")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
