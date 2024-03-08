# ROS-Package-LiDAR-Front-View-Filter
The "LiDAR Front View Filter" ROS package is designed to process raw point cloud data captured from LiDAR sensors and filter it to only include points that are within a specified front view angle, distance, and height. 
This package aims to provide a simplified and focused point cloud that can be used for navigation, obstacle avoidance, and environmental analysis in robotic applications. By concentrating on a specific region of interest, the computational load can be reduced, and the efficiency of subsequent processing stages can be improved.
# Features
- Front View Filtering: Limits the point cloud to a predefined horizontal angle, focusing on points that lie directly in front of the sensor. This is particularly useful for forward-facing applications such as autonomous vehicle navigation.
- Distance Filtering: Filters out points that are beyond a specified distance. This allows the system to focus on immediate obstacles and areas of interest, reducing noise from distant objects.
- Height Filtering: Excludes points that are above a certain height, which can be useful for ignoring overhead structures or focusing on terrain and obstacles at a vehicle's level.
- Customizable Parameters: The filter parameters, including the angle range, maximum distance, and height limit, can be easily adjusted to fit specific application needs.
- Efficient Processing: Utilizes the Point Cloud Library (PCL) for efficient point cloud processing, ensuring that the filtered point cloud is ready for use with minimal delay.
- Dependencies: Relies on pcl_ros and pcl_conversions for point cloud processing, as well as roscpp and sensor_msgs for ROS communication.
- Node: The package includes a single node that subscribes to a topic publishing raw sensor_msgs/PointCloud2 messages, processes the incoming point cloud data according to the filter settings, and publishes the filtered point cloud to a new topic.
- Input Topic: The node subscribes to /raw_point_cloud by default, which is expected to publish sensor_msgs/PointCloud2 messages.
Output Topic: The filtered point cloud is published to /filtered_point_cloud as sensor_msgs/PointCloud2 message
- Configuration: Filter parameters can be configured directly in the source code or potentially through dynamic reconfigure or ROS parameters for greater flexibility.
