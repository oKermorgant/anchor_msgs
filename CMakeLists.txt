cmake_minimum_required(VERSION 3.5)
project(anchor_msgs)

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(builtin_interfaces REQUIRED)
find_package(geometry_msgs REQUIRED)

find_package(rosidl_default_generators REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
"msg/RangeWithCovariance.msg"
DEPENDENCIES builtin_interfaces geometry_msgs)

install(DIRECTORY launch DESTINATION share/${PROJECT_NAME})

ament_package()
