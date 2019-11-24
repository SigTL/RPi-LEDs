import RPi.GPIO as GPIO
import time

# turn off warnings
GPIO.setwarnings(False)

# specifies BCM and assigns GPIO pins
GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)

# loop 50 times
for i in range(500):
    GPIO.output(17, True)
    time.sleep(.05)
    GPIO.output(17, False)
    time.sleep(.01)
    GPIO.output(18, True)
    time.sleep(.05)
    GPIO.output(18, False)
    time.sleep(.01)
    GPIO.output(22, True)
    time.sleep(.05)
    GPIO.output(22, False)
    time.sleep(.01)
    GPIO.output(23, True)
    time.sleep(.05)
    GPIO.output(23, False) 

# this is supposed to reset the GPIOs
GPIO.cleanup()
