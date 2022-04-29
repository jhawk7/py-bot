from L298N import L298N
import time

def setMotors(in1, in2, in3, in4, ena, enb):
	motor = L298N(in1, in2, in3, in4, ena, enb)
	return motor


# using GPIO pin numbers not board pin numbers
# GPIO_17 => pin 11, GPIO_27 => pin 13, GPIO_24 => pin 18, GPIO_25 => pin 22, GPIO_10 => pin 19, GPIO_9 =>21 
motor = setMotors(17, 27, 24, 25, 10, 9)

motor.forward()
time.sleep(1)
motor.stop()
time.sleep(1)
motor.backward()
time.sleep(1)
motor.stop()
time.sleep(1)
motor.rightTurn()
time.sleep(1)
motor.leftTurn()
time.sleep(1)
motor.turnAround()
time.sleep(1)
motor.turnAround()
time.sleep(1)
motor.spin()
time.sleep(1)
motor.forward()
time.sleep(5)
motor.exit()