import RPi.GPIO as GPIO

class Servo():
  def __init__(self, pin):
    self.pin = pin
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(pin, GPIO.OUT)
    self.center = 70
    self.left = 150
    self.right = -12
    self.servo = GPIO.PWM(self.pin, 50) #sets servoPin to 50Hz
    self.servo.start(0)

  def setAngle(self, angle):
    duty = angle/18 + 2
    self.servo.ChangeDutyCycle(duty)
    
  def turnRight(self):
    self.setAngle(self.right)
  
  def turnLeft(self):
    self.setAngle(self.left)
  
  def front(self):
    self.setAngle(self.center)

    