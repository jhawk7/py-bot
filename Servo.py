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
        
    def turnRight(self):
        self.servo.start(2.5)
        self.servo.ChangeDutyCycle(self.right)
        self.servo.stop()
    
    def turnLeft(self):
        self.servo.start(2.5)
        self.servo.ChangeDutyCycle(self.left)
        self.servo.stop()
    
    def center(self):
        self.servo.start(2.5)
        self.servo.ChangeDutyCycle(self.mid)
        self.servo.stop()

    