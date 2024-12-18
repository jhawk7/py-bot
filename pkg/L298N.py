import RPi.GPIO as GPIO 
import time         

#RPi.GPIO is specific to arm processors and will not work on other machines

class L298N:
  def __init__(self, in1, in2, in3, in4, ena, enb):
    self.in1 = in1
    self.in2 = in2
    self.in3 = in3
    self.in4 = in4
    self.ena = ena
    self.enb = enb

    GPIO.setmode(GPIO.BCM)
    GPIO.setup(in1,GPIO.OUT)
    GPIO.setup(in2,GPIO.OUT)
    GPIO.setup(in3,GPIO.OUT)
    GPIO.setup(in4,GPIO.OUT)
    GPIO.setup(ena,GPIO.OUT)
    GPIO.setup(enb,GPIO.OUT)
    GPIO.output(in1,GPIO.LOW)
    GPIO.output(in2,GPIO.LOW)
    GPIO.output(in3,GPIO.LOW)
    GPIO.output(in4,GPIO.LOW)

    pwm_ena=GPIO.PWM(ena,1000) #sets ena pin to 1000HZ
    pwm_enb=GPIO.PWM(enb,1000) #sets enb pin to 1000Hz
    #Default speed is low and forward
    # low=25, med=50, high=75
    pwm_ena.start(25)
    pwm_enb.start(25)


  def forward(self):
    GPIO.output(self.in1,GPIO.HIGH)
    GPIO.output(self.in2,GPIO.LOW)
    GPIO.output(self.in3,GPIO.HIGH)
    GPIO.output(self.in4,GPIO.LOW)


  def backward(self):
    GPIO.output(self.in1,GPIO.LOW)
    GPIO.output(self.in2,GPIO.HIGH)
    GPIO.output(self.in3,GPIO.LOW)
    GPIO.output(self.in4,GPIO.HIGH)


  def stop(self):
    GPIO.output(self.in1,GPIO.LOW)
    GPIO.output(self.in2,GPIO.LOW)
    GPIO.output(self.in3,GPIO.LOW)
    GPIO.output(self.in4,GPIO.LOW)


  def rightTurn(self):
    #zero radius turn
    GPIO.output(self.in1,GPIO.LOW)
    GPIO.output(self.in2,GPIO.HIGH)
    GPIO.output(self.in3,GPIO.HIGH)
    GPIO.output(self.in4,GPIO.LOW)
    time.sleep(0.5)
    self.stop()

  def leftTurn(self):
    #zero radius turn
    GPIO.output(self.in1,GPIO.HIGH)
    GPIO.output(self.in2,GPIO.LOW)
    GPIO.output(self.in3,GPIO.LOW)
    GPIO.output(self.in4,GPIO.HIGH)
    time.sleep(0.5)
    self.stop()

  def spin(self):
    #360 spin
    GPIO.output(self.in1,GPIO.HIGH)
    GPIO.output(self.in2,GPIO.LOW)
    GPIO.output(self.in3,GPIO.LOW)
    GPIO.output(self.in4,GPIO.HIGH)
    time.sleep(1.25)
    self.stop()

  def turnAround(self):
    #180 degree 0 radius turn
    GPIO.output(self.in1,GPIO.HIGH)
    GPIO.output(self.in2,GPIO.LOW)
    GPIO.output(self.in3,GPIO.LOW)
    GPIO.output(self.in4,GPIO.HIGH)
    time.sleep(.65)
    self.stop()

  def exit(self):
    GPIO.cleanup()
