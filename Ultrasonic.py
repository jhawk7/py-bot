import RPi.GPIO as GPIO
import os, signal

from time import sleep, time

class UltraSonic():
    # Ultrasonic sensor class 
    
    def __init__(self, TRIG, ECHO, offset = 0.5):
        # Create a new sensor instance
        self.TRIG = TRIG
        self.ECHO = ECHO
        self.offset = offset            # Sensor calibration factor
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.TRIG, GPIO.OUT)                  
        GPIO.setup(self.ECHO, GPIO.IN)                   


    def ping(self):
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
        distance = pulse_duration * 17150            
        distance = round(distance, 2)                    

        if distance > 2 and distance < 400:              
            distance = distance + self.offset
            print("Distance: ", distance," cm")
        else:
            distance = 0
            print("No obstacle")                         
        return distance

