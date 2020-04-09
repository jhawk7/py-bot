import time
import RPi.GPIO as GPIO
from Ultrasonic import Ultrasonic
from L298N import L298N
import threading

#Flags
OBJECT_DETECTED = False
RECOVERING = False
STOP = False

#Constants
MIN_DISTANCE = 20
MAX_DISTANCE = 100

#LED GPIO Pin
LED = 18
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

# Sonar GPIO Pins
TRIG = 22
ECHO = 23

# L298N GPIO Pins
IN1 = 17
IN2 = 27
IN3 = 24
IN4 = 25
ENA = 10
ENB = 9

sonar = Ultrasonic(TRIG, ECHO)
motor = L298N(IN1, IN2, IN3, IN4, ENA, ENB)

def detect():
	while STOP == False:
		distance = sonar.ping()
		if distance < MAX_DISTANCE and distance > MIN_DISTANCE:
			OBJECT_DETECTED = True
			RECOVERING = True
			GPIO.output(LED,GPIO.HIGH)
		else:
			OBJECT_DETECTED = False
			RECOVERING = False
			GPIO.output(LED,GPIO.LOW)

	return

def go():
	while STOP == False:
		if (not OBJECT_DETECTED and not RECOVERING and not STOP):
			motor.forward()

		elif (OBJECT_DETECTED and RECOVERING and not STOP):
			recover()
	return


def recover():
		motor.stop()
		motor.backward()
		motor.stop()
		motor.rightTurn()
		motor.stop()


def stop():
	while True:
		user_input = raw_input()
		if user_input == 'x'
			STOP = True
			motor.stop()
			goThread.join()
			detectThread.join()
			motor.exit()


print("Starting Py-bot, press 'x' to terminate...")
goThread = threading(name=goThread, threadID=1, target=go())
detectThread = threading(name=detectThread, threadID=2, target=detect())
stop()




