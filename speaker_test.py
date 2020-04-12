import RPi.GPIO as GPIO
import time

c4 = 261
d4 = 294
e4 = 329
f4 = 349
g4 = 392
a4 = 440
b4 = 493
c5 = 523.25

#speaker GPIO Pin
speaker = 21

# choose BCM or BOARD numbering schemes. I use BCM  
GPIO.setmode(GPIO.BCM)
GPIO.setup(speaker, GPIO.OUT)


def speakerTest():
	# create an object p for PWM on port 21 at 50 Hertz  
	p = GPIO.PWM(speaker, 50)
	# start the PWM on 70 percent duty cycle - defines the amount of time a signal is high (square wave)  
	p.start(70)

	for x in range(200, 2200):
		# change the frequency to x Hz
		p.ChangeFrequency(x)
		time.sleep(0.0001)

	p.stop()



def beepTest():
	p = GPIO.PWM(speaker, 50)
	p.start(70)

	beeps = [c4, d4, e4, f4, g4, a4, b4, c5]

	for note in beeps:
		p.ChangeFrequency(note)
		time.sleep(0.1)

	p.stop()



speakerTest()
beepTest()
GPIO.cleanup()