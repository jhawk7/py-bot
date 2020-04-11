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
	p = GPIO.PWM(speaker, 50)    # create an object p for PWM on port 25 at 50 Hertz  
	p.start(70)             	 # start the PWM on 70 percent duty cycle  

	while not STOP:
	#for x in range(200, 2200):
 		#p.ChangeFrequency(x)     # change the frequency to x Hz 
 		#time.sleep(0.0001)
 		p.ChangeFrequency(30)
 		p.ChangeFrequency(70)
 		p.ChangeFrequency(50)
    	p.stop()
    	time.sleep(10)
	#p.stop()                     # stop the PWM output  
	


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


