CAMERA_TYPE = "CSIC"   # (PICAM|WEBCAM|CVCAM|CSIC|V4L|MOCK)
IMAGE_W = 224
IMAGE_H = 224
CSIC_CAM_GSTREAMER_FLIP_PARM = 0 # (0 => none , 4 => Flip horizontally, 6 => Flip vertically)
# PCA9685_I2C_ADDR = 0x40     #I2C address, use i2cdetect to validate this number
PCA9685_I2C_BUSNUM = 1   #None will auto detect, which is fine on the pi. But other platforms should specify the bus num.
# #STEERING
# STEERING_CHANNEL = 1            #channel on the 9685 pwm board 0-15
# Center is 330
STEERING_LEFT_PWM = 420         #pwm value for full left steering
STEERING_RIGHT_PWM = 240        #pwm value for full right steering
# 
# #THROTTLE
# THROTTLE_CHANNEL = 0            #channel on the 9685 pwm board 0-15
THROTTLE_FORWARD_PWM = 380      #pwm value for max forward throttle
THROTTLE_STOPPED_PWM = 330      #pwm value for no movement
THROTTLE_REVERSE_PWM = 280      #pwm value for max reverse throttle
# #JOYSTICK
# USE_JOYSTICK_AS_DEFAULT = True     #when starting the manage.py, when True, will not require a --js option to use the joystick
# CONTROLLER_TYPE='F7100'               #(ps3|ps4|xbox|nimbus|wiiu|F710|rc3)
