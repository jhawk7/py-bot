import RPi.GPIO as GPIO
from Servo import Servo
from time import sleep, time

class UltrasonicServo():
    # UltrasonicServo sensor class 
    
    def __init__(self, TRIG, ECHO, MIN_DIST=0, SERVO=14, offset = 0.5):
        # Create a new sensor instance
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.MIN_DIST = MIN_DIST
        self.servo = Servo(SERVO)
        self.offset = offset            # Sensor calibration factor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)                  
        GPIO.setup(self.ECHO, GPIO.IN)                   


    def objectDetected(self):
        # Get distance measurement
        GPIO.output(self.TRIG, GPIO.LOW)            # Set TRIG LOW
        sleep(0.1)                                  # Min gap between measurements        
        # Create 10 us pulse on TRIG
        GPIO.output(self.TRIG, GPIO.HIGH)           # Set TRIG HIGH
        sleep(0.00001)                              # Delay 10 us
        GPIO.output(self.TRIG, GPIO.LOW)            # Set TRIG LOW
        # Measure return echo pulse duration
        while GPIO.input(self.ECHO) == GPIO.LOW:    
            pulse_start = time()                         

        while GPIO.input(self.ECHO) == GPIO.HIGH:        
            pulse_end = time()                           

        pulse_duration = pulse_end - pulse_start 
        # Distance = 17160.5 * Time (unit cm) at sea level and 20C
        distance = pulse_duration * 17160.5            
        distance = round(distance, 2)                    

        if distance > 2 and distance < 400:              
            distance = distance + self.offset
            print("Obstacle Distance: #{distance} cm")
        else:
            distance = 0
            #print("No obstacle")                         
        
        if distance <= self.MIN_DIST and distance != 0:
            return True
        else:
            return False
    
    def checkLeft(self):
        self.servo.turnLeft()
        sleep(2)
        left = self.objectDetected()
        self.servo.front()
        sleep(1)
        return left
    
    def checkRight(self):
        self.servo.turnRight()
        sleep(2)
        right = self.objectDetected()
        self.servo.front()
        sleep(1)
        return right

    def checkFront(self):
        self.servo.front()
        sleep(2)
        front = self.objectDetected()
        sleep(1)
        return front

