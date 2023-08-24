#!/usr/bin/env python3

import rclpy
from rclpy.node import Node
from sensor_msgs.msg import TimeReference
from rclpy import clock
TOPIC_NAME = "rpi_time/clock"


class RpiTimePublisher(Node):

    def __init__(self):
        super().__init__('rpi_time_publisher')
        self.publisher_ = self.create_publisher(TimeReference, TOPIC_NAME, 10)
        self.timer = self.create_timer(1/30, self.timer_callback)

    def timer_callback(self):
        msg = TimeReference()
        wall_time = clock.Clock(
            clock_type=clock.ClockType(2)).now().to_msg()  # 2 => System time
        msg.header.stamp = wall_time
        msg.header.frame_id = "clock"
        msg.time_ref = wall_time
        msg.source = "rpi clock"
        self.publisher_.publish(msg)


def main():
    rclpy.init()

    rpi_time_publisher = RpiTimePublisher()

    rclpy.spin(rpi_time_publisher)

    rpi_time_publisher.destroy_node()
    rclpy.shutdown()


if __name__ == "__main__":
    main()
