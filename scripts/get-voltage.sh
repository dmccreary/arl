!#/bin/sh
# use this to get the voltage supplied to the computer
# The voltage should be close to 5.0.  A value of 4.9 or less means the NVIDIA Nano must be less
cat /sys/bus/i2c/drivers/ina3221x/[0–9]-[0–9][0–9][0–9][0–9]/iio\:device0/in_voltage*
