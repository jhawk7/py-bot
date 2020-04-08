from adafruit_circuitpython_hcsr04 import HCSR04
import time
import RPi.GPIO as GPIO

MIN_DISTANCE = 35

def sonarTest(trigger, echo):
	# GPIO_18 => pin 12
	LED = 18
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(LED,GPIO.OUT)
	sonar = HCSR04(trigger_pin=trigger, echo_pin=echo)

	while True:
		try:
			if sonar.distance > MIN_DISTANCE:
				GPIO.output(LED, GPIO.HIGH)
				print((sonar.distance))
		except RuntimeError:
			print("Retrying!")
		time.sleep(0.1)

# using GPIO pin numbers opposed to board pin numbers
sonarTest(3, 4)


