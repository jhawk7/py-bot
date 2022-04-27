import time
import RPi.GPIO as GPIO

servoPIN = 14
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

def testServo():
    p = GPIO.PWM(servoPIN, 50) #sets servoPin to 50Hz
    p.start(2.5)
    cycles = [5, 7.5, 10, 12.5, 10, 7.5, 5, 2.5]

    for cycle in cycles:
        p.ChangeDutyCycle(cycle)
        time.sleep(0.5)
    
    p.stop()
    GPIO.cleanup()


testServo()
