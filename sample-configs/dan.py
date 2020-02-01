# #CAMERA
CAMERA_TYPE = "CSIC"   # (PICAM|WEBCAM|CVCAM|CSIC|V4L|MOCK)
IMAGE_W = 240
IMAGE_H = 240
CAMERA_VFLIP = True
# CAMERA_HFLIP = False
# # For CSIC camera - If the camera is mounted in a rotated position, changing the below parameter will correct the output frame orientation
CSIC_CAM_GSTREAMER_FLIP_PARM = 6 # (0 => none , 4 => Flip horizontally, 6 => Flip vertically)
# 
PCA9685_I2C_BUSNUM = 1   #None will auto detect, which is fine on the pi. But other platforms should specify the bus num.
# 
# #STEERING
# STEERING_CHANNEL = 1            #channel on the 9685 pwm board 0-15
STEERING_LEFT_PWM = 450         #pwm value for full left steering
STEERING_RIGHT_PWM = 260        #pwm value for full right steering
# 
# #THROTTLE
# THROTTLE_CHANNEL = 0            #channel on the 9685 pwm board 0-15
THROTTLE_FORWARD_PWM = 380      #pwm value for max forward throttle
THROTTLE_STOPPED_PWM = 330      #pwm value for no movement
THROTTLE_REVERSE_PWM = 280      #pwm value for max reverse throttle
# 
# #TRAINING
# 
# # Region of interst cropping
# # only supported in Categorical and Linear models.
# # If these crops values are too large, they will cause the stride values to become negative and the model with not be valid.
# ROI_CROP_TOP = 0                    #the number of rows of pixels to ignore on the top of the image
# ROI_CROP_BOTTOM = 0                 #the number of rows of pixels to ignore on the bottom of the image
# 
# #JOYSTICK
USE_JOYSTICK_AS_DEFAULT = True     #when starting the manage.py, when True, will not require a --js option to use the joystick
# JOYSTICK_MAX_THROTTLE = 0.5         #this scalar is multiplied with the -1 to 1 throttle value to limit the maximum throttle. This can help if you drop the controller or just don't need the full speed available.
# JOYSTICK_STEERING_SCALE = 1.0       #some people want a steering that is less sensitve. This scalar is multiplied with the steering -1 to 1. It can be negative to reverse dir.
# AUTO_RECORD_ON_THROTTLE = True      #if true, we will record whenever throttle is not zero. if false, you must manually toggle recording with some other trigger. Usually circle button on joystick.
CONTROLLER_TYPE='F710'               #(ps3|ps4|xbox|nimbus|wiiu|F710|rc3)
# USE_NETWORKED_JS = False            #should we listen for remote joystick control over the network?
# NETWORK_JS_SERVER_IP = "192.168.0.1"#when listening for network joystick control, which ip is serving this information
# JOYSTICK_DEADZONE = 0.0             # when non zero, this is the smallest throttle before recording triggered.
# JOYSTICK_THROTTLE_DIR = -1.0        # use -1.0 to flip forward/backward, use 1.0 to use joystick's natural forward/backward
