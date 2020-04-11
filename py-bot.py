import time
import RPi.GPIO as GPIO
from Ultrasonic import Ultrasonic
from L298N import L298N
import threading

#Flags
OBJECT_DETECTED = None
RECOVERING = None
STOP = None
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
	global OBJECT_DETECTED
	global RECOVERING
	global STOP

	while not STOP:
		distance = sonar.ping()
		if distance <= MAX_DISTANCE and distance != 0 and not RECOVERING:
			OBJECT_DETECTED = True
			GPIO.output(LED,GPIO.HIGH)
		else:
			OBJECT_DETECTED = False

		time.sleep(0.5)

	return

def go():
	global OBJECT_DETECTED
	global RECOVERING
	global STOP

	while not STOP:
		if (not OBJECT_DETECTED and not RECOVERING):
			motor.forward()
		else:
			motor.stop()

	return


def recover():
	global OBJECT_DETECTED
	global RECOVERING
	global STOP

	while not STOP:
		while OBJECT_DETECTED:
			RECOVERING = True
			print("Avoiding Obstacle..")
			motor.stop()
			motor.backward()
			motor.stop()
			motor.rightTurn()
			motor.stop()
			GPIO.output(LED,GPIO.LOW)
			print("Obstacle Avoided..")
		
		RECOVERING = False


def stop():
	global STOP

	user_input = input()
	if user_input != None:
		STOP = True
		motor.stop()
		motor.exit()
	return


print("Starting Py-bot..press any key to terrminate.")

goThread = threading.Thread(target=go)
detectThread = threading.Thread(target=detect)
recoverThread = threading.Thread(target=recover)
stopThread = threading.Thread(target=stop)

goThread.daemon = True
detectThread.daemon = True
recoverThread.daemon = True
stopThread.daemon = True

goThread.start()
detectThread.start()
recoverThread.start()
stopThread.start()

#goThread.join()
#detectThread.join()
#recoverThread.join()
stopThread.join()

print("Py-bot terminated.")


