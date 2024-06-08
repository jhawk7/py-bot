from pkg.UltrasonicServo import UltrasonicServo
import time
import RPi.GPIO as GPIO

# Sonar GPIO Pins
TRIG = 22
ECHO = 23
SERVO = 14 #sonar servo pin
MIN_DISTANCE = 40 #in cm

def lookTest():
    sonar_servo = UltrasonicServo(TRIG, ECHO, MIN_DISTANCE, SERVO)
    left = sonar_servo.checkLeft()
    print("Object detected in range on left") if left else print("No object in range on left")
    time.sleep(1)
    right = sonar_servo.checkRight()
    print("Object detected in range on right") if right else print("No object in range on right")
    time.sleep(1)
    center = sonar_servo.checkFront()
    print("Object detected in range in front") if center else print("No object in range in front")
    return
#

lookTest()
GPIO.cleanup()
