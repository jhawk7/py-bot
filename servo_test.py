import time
import RPi.GPIO as GPIO
from Servo import Servo

servoPIN = 14

def testServo():
    servo = Servo(servoPIN)
    servo.center()
    time.sleep(1)
    servo.turnLeft()
    time.sleep(1)
    servo.center()
    time.sleep(1)
    servo.turnRight()
    time.sleep(1)
    servo.center()
    time.sleep(1)
    
   # p.stop()
    GPIO.cleanup()


testServo()
