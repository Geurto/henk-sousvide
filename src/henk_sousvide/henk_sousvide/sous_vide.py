#!/usr/bin/env python3
import rclpy
from rclpy.node import Node

import random


class SousVide(Node):
    def __init__(self, node_name: str, **kwargs):
        super().__init__(node_name)


def main(args=None):
    rclpy.init(args=args)

    node = SousVide("sous_vide")
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == "__main__":
    main()
