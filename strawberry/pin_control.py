import sys
import RPi.GPIO as GPIO

# GPIO setup
GPIO.setmode(GPIO.BCM)
relay_pin = int(sys.argv[1])
state = sys.argv[2]
GPIO.setup(relay_pin, GPIO.OUT)

print(111)

if state == 'on':
    GPIO.output(relay_pin, GPIO.HIGH)
elif state == 'off':
    GPIO.output(relay_pin, GPIO.LOW)
