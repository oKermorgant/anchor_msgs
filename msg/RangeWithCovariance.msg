# This is the possibly noised measured range [m] between two frames:
# - header.frame_id: the frame of the beacon
# - moving_frame: the frame attached to the robot

std_msgs/Header header
string moving_frame
float64 range
float64 range_min 0.
float64 range_max 100.
float64 covariance 0.01
