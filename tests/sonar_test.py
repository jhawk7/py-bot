import time
import RPi.GPIO as GPIO
from Pkg.UltrasonicServo import UltrasonicServo

MIN_DISTANCE = 2 #value in cm

def sonarTest(trigger, echo):
	# GPIO_18 => pin 12
	LED = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED,GPIO.OUT)
	sonar = UltrasonicServo(trigger, echo)

	while True:
		try:
			objectDetected = sonar.objectDetected()
			if objectDetected:
				#LED will turn on when object is detected 
				GPIO.output(LED,GPIO.HIGH)
			else:
				GPIO.output(LED,GPIO.LOW)
		except RuntimeError:
			print("Retrying!")
		time.sleep(0.1)


# using GPIO pin numbers opposed to board pin numbers
#GPIO_22 => pin 15; GPIO_23 => pin 16
sonarTest(22, 23)


