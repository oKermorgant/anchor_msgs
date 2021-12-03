from simple_launch import SimpleLauncher

def generate_launch_description():
    sl = SimpleLauncher()
    
    sl.declare_gazebo_axes()
    sl.declare_arg('anchor_frame','anchor','Name of the anchor frame')
    sl.declare_arg('reference_frame','map','Name of the reference frame')
    
    sl.node('tf2_ros','static_transform_publisher',name=sl.name_join(sl.arg('anchor_frame'),'_tf'),
            arguments = [sl.arg('x'),sl.arg('y'),sl.arg('z'),
                        sl.arg('yaw'),sl.arg('pitch'),sl.arg('roll'),
                        sl.arg('reference_frame'),sl.arg('anchor_frame')])
    return sl.launch_description() 
