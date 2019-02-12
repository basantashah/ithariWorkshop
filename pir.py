import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(3, GPIO.OUT)         #LED output pin
while True:
	i=GPIO.input(11)
	if i==0:                 #When output from motion sensor is LOW
		print "No intruders",i
		GPIO.output(8, GPIO.HIGH) # Turn on
		sleep(1) # Sleep for 1 second
		GPIO.output(8, GPIO.LOW) # Turn off
		sleep(1) # Sleep for 1 second
