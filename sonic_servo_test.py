from UltrasonicServo import UltrasonicServo
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
    print("Object detected on left") if left else print("No object on left")
    time.sleep(1)
    right = sonar_servo.checkRight()
    print("Object detected on right") if right else print("No object on right")
    time.sleep(1)
    center = sonar_servo.checkFront()
    print("Object detected on center") if center else print("No object in front")
    return
#

lookTest()
GPIO.cleanup()
