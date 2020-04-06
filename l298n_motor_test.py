from L298N import L298N
from time import sleep, time

def motorTest(in1, in2, in3, in4, ena, enb):
	motor = L298N(in1, in2, in3, in4, ena, enb)
	motor.forward()
	time.sleep(0.1)
	motor.stop()
	time.sleep(0.1)
	motor.backward()
	time.sleep(0.1)
	motor.stop()
	time.sleep(0.1)
	motor.exit()

# using GPIO pin numbers not board pin numbers
# GPIO_17 => pin 11, GPIO_27 => pin 13, GPIO_24 => pin 18, GPIO_25 => pin 22, GPIO_10 => pin 19, GPIO_9 =>21 
motorTest(17, 27, 24, 25, 10, 9)