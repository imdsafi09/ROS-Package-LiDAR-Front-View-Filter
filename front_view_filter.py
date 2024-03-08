#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import math

class LiDARFrontViewFilter:
    def __init__(self):
        rospy.init_node('lidar_front_view_filter', anonymous=True)
        self.pub = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)
        rospy.Subscriber('/ouster/points', PointCloud2, self.callback)
        rospy.spin()

    def callback(self, msg):
        filtered_points = []
        for point in pc2.read_points(msg, skip_nans=True):
            x, y, z = point[:3]
            angle = math.atan2(y, x)
            distance = math.sqrt(x**2 + y**2)

            # Filter based on angle and distance (e.g., front 120 degrees and up to 10m)
            if -math.radians(145/2) <= angle <= math.radians(145/2) and distance <= 50 and z <= 5:
                filtered_points.append((x, y, z))

        header = msg.header
        fields = [PointField('x', 0, PointField.FLOAT32, 1),
                  PointField('y', 4, PointField.FLOAT32, 1),
                  PointField('z', 8, PointField.FLOAT32, 1)]
        filtered_cloud = pc2.create_cloud(header, fields, filtered_points)
        self.pub.publish(filtered_cloud)

if __name__ == '__main__':
    try:
        LiDARFrontViewFilter()
    except rospy.ROSInterruptException:
        pass

#!/usr/bin/env python

import rospy
from sensor_msgs.msg import PointCloud2, PointField
import sensor_msgs.point_cloud2 as pc2
import math

class LiDARFrontViewFilter:
    def __init__(self):
        rospy.init_node('lidar_front_view_filter', anonymous=True)
        self.pub = rospy.Publisher('/filtered_point_cloud', PointCloud2, queue_size=10)
        rospy.Subscriber('/raw_point_cloud', PointCloud2, self.callback)
        rospy.spin()

    def callback(self, msg):
        filtered_points = []
        for point in pc2.read_points(msg, skip_nans=True):
            x, y, z = point[:3]
            angle = math.atan2(y, x)
            distance = math.sqrt(x**2 + y**2)

            # Filter based on a 145-degree angle range, distance up to 50 meters,
            # and height up to 5 meters
            if -math.radians(145/2) <= angle <= math.radians(145/2) and distance <= 50 and z <= 5:
                filtered_points.append((x, y, z))

        header = msg.header
        fields = [PointField('x', 0, PointField.FLOAT32, 1),
                  PointField('y', 4, PointField.FLOAT32, 1),
                  PointField('z', 8, PointField.FLOAT32, 1)]
        filtered_cloud = pc2.create_cloud(header, fields, filtered_points)
        self.pub.publish(filtered_cloud)

if __name__ == '__main__':
    try:
        LiDARFrontViewFilter()
    except rospy.ROSInterruptException:
        pass

