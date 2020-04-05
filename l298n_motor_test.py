import l298n
import RPi.GPIO as GPIO

def motorTest(pin1, pin2):
	motor = l298n(pin1, pin2)
	motor.forwards()
	motor.backwards()
	motor.stop()

# using GPIO pin numbers not board pin numbers
motorTest(17, 27)

