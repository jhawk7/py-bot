import time
import RPi.GPIO as GPIO
from Ultrasonic import Ultrasonic
from L298N import L298N
from threading import Thread

#Flags
OBJECT_DETECTED = False
#RECOVERING = False
STOP = False
#Constants
MAX_DISTANCE = 40 #in cm

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
		if distance <= MAX_DISTANCE and distance != 0:
			OBJECT_DETECTED = True
			GPIO.output(LED,GPIO.HIGH)
		else:
			OBJECT_DETECTED = False
			GPIO.output(LED,GPIO.LOW)
		time.sleep(0.5)

	return

def go():
	while not STOP:
		if (not OBJECT_DETECTED):
			motor.forward()
		else:
			motor.stop()
	return


def recover():
	while not STOP:
		while OBJECT_DETECTED:
			print("Avoiding Obstacle..")
			motor.stop()
			motor.backward()
			motor.stop()
			motor.rightTurn()
			motor.stop()
			print("Obstacle Avoided..")
	return

def stop():
	user_input = input()
	if user_input != None:
		STOP = True
		motor.stop()
		motor.exit()
	return


print("Starting Py-bot..press any key to terrminate.")

goThread = Thread(target=go)
detectThread = Thread(target=detect)
recoverThread = Thread(target=recover)
stopThread = Thread(target=stop)

goThread.start()
detectThread.start()
recoverThread.start()
#stopThread.start()

goThread.join()
detectThread.join()
recoverThread.join()
stopThread.join()

print("Py-bot terminated.")


