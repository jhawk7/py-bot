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

#Speaker GPIO Pin
speaker = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(speaker, GPIO.OUT)

#notes in hz
c4 = 261
d4 = 294
e4 = 329
f4 = 349
g4 = 392
a4 = 440
b4 = 493
c5 = 523.25
d5 = 587.33

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


def beep():
	beeps = [e4, d4, g4, d5, a4]
	p = GPIO.PWM(speaker, 100)

	while not STOP:
		p.start(10)
		for beep in beeps:
			p.ChangeFrequency(beep)
			time.sleep(0.1)

		p.stop()
		time.sleep(20)

	return


def detect():
	global OBJECT_DETECTED
	global RECOVERING
	global STOP

	while not STOP:
		distance = sonar.ping()
		if distance <= MAX_DISTANCE and distance != 0 and not RECOVERING:
			OBJECT_DETECTED = True
			GPIO.output(LED,GPIO.HIGH)
			time.sleep(0.5)

	return

def go():
	global OBJECT_DETECTED
	global STOP

	while not STOP:
		if (not OBJECT_DETECTED):
			motor.forward()
		else:
			motor.stop()
			time.sleep(0.5)
			recover()
	return


def recover():
	global OBJECT_DETECTED
	global RECOVERING
	global STOP

	RECOVERING = True
	print("Avoiding Obstacle..")
	motor.backward()
	time.sleep(0.5)
	motor.stop()
	time.sleep(0.5)
	motor.rightTurn()
	time.sleep(0.5)
	motor.stop()
	GPIO.output(LED,GPIO.LOW)
	print("Obstacle Avoided..")
	RECOVERING = False
	OBJECT_DETECTED = False
	time.sleep(0.5)


def stop():
	global STOP

	user_input = input()
	if user_input != None:
		STOP = True
		motor.stop()
		GPIO.cleanup()
	return


print("Starting Py-bot..press any key to terrminate.")

goThread = threading.Thread(target=go)
detectThread = threading.Thread(target=detect)
stopThread = threading.Thread(target=stop)
beepThread = threading.Thread(target=beep)

goThread.daemon = True
detectThread.daemon = True
stopThread.daemon = True
beepThread.daemon = True

goThread.start()
detectThread.start()
stopThread.start()
beepThread.start()

stopThread.join()

print("Py-bot terminated.")


