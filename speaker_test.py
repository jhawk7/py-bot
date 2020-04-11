import RPi.GPIO as GPIO
import time

def speakerTest():
	GPIO.setmode(GPIO.BCM)  # choose BCM or BOARD numbering schemes. I use BCM  
	GPIO.setup(21, GPIO.OUT)# set GPIO 25 as an output. You can use any GPIO port  
	p = GPIO.PWM(21, 50)    # create an object p for PWM on port 25 at 50 Hertz  
	p.start(70)             # start the PWM on 70 percent duty cycle  

	for x in range(200, 2200):
 		p.ChangeFrequency(x)  # change the frequency to x Hz 
 		time.sleep(0.0001)
    
	p.stop()                # stop the PWM output  
	#GPIO.cleanup()          # when your program exits, tidy up after yourself


def beep():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(21, GPIO.OUT)
	p = GPIO.PWM(21, 50)
	p.start(70)
	p.ChangeFrequency(30)
	time.sleep(0.001)
	p.ChangeFrequency(70)
	time.sleep(0.001)
	p.ChangeFrequency(50)
	time.sleep(0.001)
	p.stop()


speakerTest()
beep()
GPIO.cleanup()