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

GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
GPIO.setup(speaker, GPIO.OUT) # set GPIO 25 as an output. You can use any GPIO port


def speakerTest():  
	p = GPIO.PWM(speaker, 50)    # create an object p for PWM on port 25 at 50 Hertz  
	p.start(70)             # start the PWM on 70 percent duty cycle - defines the amount of time a signal is high (square wave)  

	for x in range(200, 2200):
 		p.ChangeFrequency(x)  # change the frequency to x Hz 
 		time.sleep(0.0001)

 	p.stop()



def beepTest():
	p = GPIO.PWM(speaker, 100)
	p.start(10)

	beeps = [c4, d4, e4, f4, g4, a4, b4, c5]

	for note in beeps:
		p.ChangeFrequency(note)
		time.sleep(0.1)

	p.stop()



speakerTest()
beepTest()
GPIO.cleanup()