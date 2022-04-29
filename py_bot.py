import sys
import time
import RPi.GPIO as GPIO
from UltrasonicServo import UltrasonicServo
from L298N import L298N
import threading

#Flags
OBJECT_DETECTED = False
RECOVERING = False
STOP = False

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
    while True:
        if STOP:
            break
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

	while True:
		if STOP:
			break
		while not RECOVERING:
			OBJECT_DETECTED = sonar_servo.objectDetected()
			if OBJECT_DETECTED:
				GPIO.output(LED,GPIO.HIGH)
				time.sleep(0.5)	
			else:
				GPIO.output(LED,GPIO.LOW)
				time.sleep(0.5)
	return


def go():
	global OBJECT_DETECTED
	global STOP
	global RECOVERING

	while True:
		if STOP:
			break
		while not RECOVERING:
			if OBJECT_DETECTED:
				motor.stop()
				time.sleep(0.5)
				RECOVERING = True
				recover()
			else:
				motor.forward()
	return


def recover():
    global RECOVERING
    global STOP
    
    while RECOVERING:
        if STOP:
            break
        print("taking evasive maneuvers..")
        motor.backward()
        time.sleep(0.5)
        motor.stop()
        time.sleep(0.5)
        
        if not sonar_servo.checkRight():
            motor.rightTurn()
            time.sleep(1)
        elif not sonar_servo.checkLeft():
            motor.leftTurn()
            time.sleep(1)
        else:
            motor.turnAround()
            time.sleep(1)
        
        RECOVERING = False
        print("path clear..")
        time.sleep(1)


def stop():
	global STOP
	user_input = input()
	if user_input != None:
		STOP = True
		motor.stop()
		sonar_servo.reset()
		GPIO.cleanup()
	return


def main():
	print("Starting py-bot..press any key to terrminate.")
	GPIO.setwarnings(False)
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
	goThread.join()
	detectThread.join()
	beepThread.join()
	print("py-bot terminated.")
	sys.exit()

if __name__ == '__main__':
	main()
