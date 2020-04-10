import time
import RPi.GPIO as GPIO
from Ultrasonic import Ultrasonic
from L298N import L298N
from threading import Thread

#Flags
OBJECT_DETECTED = False
RECOVERING = False
STOP = False
user_input = input()
#Constants
MAX_DISTANCE = 30 #in cm

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
		if distance <= MAX_DISTANCE:
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
		print("Avoiding Obstacle..")
		RECOVERING = True
		motor.stop()
		motor.backward()
		motor.stop()
		motor.rightTurn()
		motor.stop()
		RECOVERING = False
		print("Obstacle Avoided..")
	return

def stop():
	while True:
		if user_input != None:
			STOP = True
			motor.stop()
			motor.exit()
		break
	return


print("Starting Py-bot..press any key to terrminate.")

goThread = Thread(target=go)
detectThread = Thread(target=detect)
recoverThread = Thread(target=recover)
stopThread = Thread(target=stop)
goThread.start()
detectThread.start()
recoverThread.start()
stopThread.start()

goThread.join()
detectThread.join()
recoverThread.join()
stopThread.join()

print("Py-bot terminated.")


