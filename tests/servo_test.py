import time
import RPi.GPIO as GPIO
from pkg.Servo import Servo

servoPIN = 14

def testServo():
    servo = Servo(servoPIN)
    servo.front()
    time.sleep(1)
    servo.turnLeft()
    time.sleep(1)
    servo.front()
    time.sleep(1)
    servo.turnRight()
    time.sleep(1)
    servo.front()
    time.sleep(1)
    
   # p.stop()
    GPIO.cleanup()


testServo()
