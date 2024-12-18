import sys
import time
import RPi.GPIO as GPIO
from pkg.UltrasonicServo import UltrasonicServo
from pkg.L298N import L298N
import threading

#Flags
OBJECT_DETECTED = False
RECOVERING = False
STOP = False

#Locks
sonarLock = threading.Lock()
motorLock = threading.Lock()

#Constants
MIN_DISTANCE = 40 #in cm

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

# Sonar Servo Pin
SERVO = 14

# L298N GPIO Pins
IN1 = 17
IN2 = 27
IN3 = 24
IN4 = 25
ENA = 10
ENB = 9

sonar_servo = UltrasonicServo(TRIG, ECHO, MIN_DISTANCE, SERVO)
motor = L298N(IN1, IN2, IN3, IN4, ENA, ENB)

def beep():
	global STOP
	beeps = [e4, d4, d5, a4]
	p = GPIO.PWM(speaker, 100)
	while not STOP:
		p.start(10)
		for beep in beeps:
			p.ChangeFrequency(beep)
			time.sleep(0.1)
		
		p.stop()
		time.sleep(15)
	return


def detect():
	global OBJECT_DETECTED
	global RECOVERING
	global STOP

	while not STOP:
		while not RECOVERING and not OBJECT_DETECTED:
			with sonarLock:
				OBJECT_DETECTED = sonar_servo.objectDetected()
				time.sleep(0.5)
	return


def go():
	global OBJECT_DETECTED
	global STOP
	global RECOVERING

	while not STOP:
		with motorLock:
			if OBJECT_DETECTED:
				motor.stop()
				GPIO.output(LED,GPIO.HIGH)
				time.sleep(0.2)
				RECOVERING = True
				recover()
				GPIO.output(LED,GPIO.LOW)
				OBJECT_DETECTED = False
				time.sleep(1)
			else:
				motor.forward()
				time.sleep(0.2)
	return


def recover():
	global RECOVERING
	global STOP
	
	while RECOVERING and not STOP:
		print("taking evasive maneuvers..")
		motor.backward()
		time.sleep(1)
		motor.stop()
		time.sleep(1)
		with sonarLock:
			if not sonar_servo.checkRight():
				print("turning right..")
				motor.rightTurn()
				time.sleep(1)
			elif not sonar_servo.checkLeft():
				print("turning left..")
				motor.leftTurn()
				time.sleep(1)
			else:
				print("turning around..")
				motor.turnAround()
				time.sleep(1)

		RECOVERING = False
		print("path clear..")
		time.sleep(1)
	return


def stop():
	global STOP
	while not STOP:
		user_input = input()
		if user_input != None:
			STOP = True
			print("stopping..")
			with motorLock:
				motor.stop()
			with sonarLock:
				sonar_servo.reset()
			GPIO.cleanup()
			break

		time.sleep(0.5)
	return


def main():
	print("Starting py-bot..press any key to terrminate.")
	GPIO.setwarnings(False)
	goThread = threading.Thread(target=go)
	detectThread = threading.Thread(target=detect)
	stopThread = threading.Thread(target=stop)
	beepThread = threading.Thread(target=beep)
	threads = [beepThread, goThread, detectThread, stopThread]

	for thread in threads:
		thread.daemon = True
		thread.start()
	
	for thread in threads:
		thread.join()

	print("py-bot terminated.")
	sys.exit()

if __name__ == '__main__':
	main()
