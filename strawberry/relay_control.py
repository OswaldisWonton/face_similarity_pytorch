from flask import Flask, request
import RPi.GPIO as GPIO

app = Flask(__name__)

# GPIO setup
GPIO.setmode(GPIO.BCM)
relay_pin = 17
GPIO.setup(relay_pin, GPIO.OUT)

@app.route('/control', methods=['POST'])
def control():
    state = request.form.get('state')
    if state == 'on':
        GPIO.output(relay_pin, GPIO.HIGH)
    elif state == 'off':
        GPIO.output(relay_pin, GPIO.LOW)
    return 'OK'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
