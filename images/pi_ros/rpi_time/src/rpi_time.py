#!/usr/bin/env python3

import time
import rospy
from std_msgs.msg import Bool
from sensor_msgs.msg import TimeReference

TOPIC_CONNECTION = "/rpi_time/connection"
TOPIC_NAME = "rpi_time/clock"
FRAME_ID = "clock"


if __name__ == "__main__":

    rospy.init_node("rpi_time", anonymous=True, disable_signals=False)

    time_pub = rospy.Publisher(TOPIC_NAME, TimeReference, queue_size=20)
    conn_pub = rospy.Publisher(TOPIC_CONNECTION, Bool, queue_size=1)

    connected = False
    time_rate = rospy.Rate(30)

    rospy.loginfo("Started to publish time from RPI")
    rospy.loginfo(" - topic: \"{}\"".format(TOPIC_NAME))

    while not rospy.is_shutdown():

        wall_time = rospy.Time.from_sec(time.time())
        rpi_t = TimeReference()
        rpi_t.header.stamp = wall_time
        rpi_t.header.frame_id = FRAME_ID
        rpi_t.time_ref = wall_time
        rpi_t.source = "rpi clock"
        time_pub.publish(rpi_t)

        # Publish a connection status to the ipb_car_launch system manager
        if not connected and conn_pub.get_num_connections() > 0:
            conn_pub.publish(True)
            connected = True

        time_rate.sleep()

    rospy.loginfo(" - node stopped")

