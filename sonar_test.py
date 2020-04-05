from adafruit_circuitpython_hcsr04 import HCSR04

def sonarTest(trigger, echo):
	sonar = HCSR04(trigger_pin=trigger, echo_pin=echo)

	while True:
		try:
			print((sonar.distance))
		except RuntimeError:
			print("Retrying!")
		time.sleep(0.1)

# using GPIO pin numbers opposed to board pin numbers
sonarTest(3, 4)