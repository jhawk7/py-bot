import time
import RPi.GPIO as GPIO
from Ultrasonic import Ultrasonic
from L298N import L298N
from threading import Thread

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
	while not STOP:
		distance = sonar.ping()
		if distance < MAX_DISTANCE and distance > MIN_DISTANCE:
			OBJECT_DETECTED = True
			GPIO.output(LED,GPIO.HIGH)
		else:
			OBJECT_DETECTED = False
			GPIO.output(LED,GPIO.LOW)

	return

def go():
	while not STOP:
		if (not OBJECT_DETECTED and not RECOVERING):
			motor.forward()

	return


def recover():
	while OBJECT_DETECTED and not STOP:
		RECOVERING = True
		motor.stop()
		motor.backward()
		motor.stop()
		motor.rightTurn()
		motor.stop()
		RECOVERING = False
	return

def stop():
	user_input = raw_input()
	while True:
		if user_input == 'x':
			STOP = True
			motor.stop()
			goThread.join()
			detectThread.join()
			motor.exit()
			return



print("Starting Py-bot, press 'x' to terminate...")

goThread = Thread(target=go())
detectThread = Thread(target=detect())
recoverThread = Thread(target=recover())
goThread.start()
detectThread.start()
recoverThread.start()
stop()




