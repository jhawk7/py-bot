import time
import RPi.GPIO as GPIO

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

def testServo():
    p = GPIO.PWM(servoPIN, 50) #sets servoPin to 50Hz
    p.start(2.5)
    mid = 7.5
    left_pivot = 10
    right_pivot = 5
    left = 12.5
    right = 2.5
    cycles = [mid, left_pivot, left, left_pivot, mid, right_pivot, right, right_pivot, mid]

    for cycle in cycles:
        p.ChangeDutyCycle(cycle)
        time.sleep(1)
    
    p.stop()
    GPIO.cleanup()


testServo()
