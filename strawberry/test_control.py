import sys
import time
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)

for relay_pin in range(40):
    print(relay_pin)
    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(relay_pin, GPIO.LOW)
