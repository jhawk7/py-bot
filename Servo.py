import RPi.GPIO as GPIO

class Servo():
    def __init__(self, pin):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.mid = 7.5
        self.left = 12.5
        self.right = 2.5
        self.left_pivot = 10
        self.right_pivot = 5

    def turnRight(self):
        servo = GPIO.PWM(pin, 50) #sets servoPin to 50Hz
        servo.start(2.5)
        servo.ChangeDutyCycle(self.right)
    
    def turnLeft(self):
        servo = GPIO.PWM(pin, 50) #sets servoPin to 50Hz
        servo.start(2.5)
        servo.ChangeDutyCycle(self.left)
    
    def center(self):
        servo = GPIO.PWM(pin, 50) #sets servoPin to 50Hz
        servo.start(2.5)
        servo.ChangeDutyCycle(self.mid)

    