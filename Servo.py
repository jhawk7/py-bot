import RPi.GPIO as GPIO

class Servo():
    def __init__(self, pin):
        self.pin = pin
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(pin, GPIO.OUT)
        self.mid = 7.5
        self.left = 12.5
        self.right = 2.5
        self.left_pivot = 10
        self.right_pivot = 5
        self.servo = GPIO.PWM(self.pin, 50) #sets servoPin to 50Hz
        self.servo.start(2.5)
        
    def turnRight(self):
        self.servo.ChangeDutyCycle(self.right)
    
    def turnLeft(self):
        self.servo.ChangeDutyCycle(self.left)
    
    def center(self):
        self.servo.ChangeDutyCycle(self.mid)

    