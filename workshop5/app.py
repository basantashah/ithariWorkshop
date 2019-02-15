import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# define actuators GPIOs
ledRed = 13
ledGrn = 26
# initialize GPIO status variables

ledRedSts = 0
ledGrnSts = 0

# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)
GPIO.setup(ledGrn, GPIO.OUT)
# turn leds OFF
GPIO.output(ledRed, GPIO.LOW)
GPIO.output(ledGrn, GPIO.LOW)


@app.route("/")
def index():
    # Read GPIO Status
    ledRedSts = GPIO.input(ledRed)
    ledGrnSts = GPIO.input(ledGrn)
    templateData = {
        'ledRed': ledRedSts,
        'ledGrn': ledGrnSts,
    }
    return render_template('index.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        actuator = ledRed
    if deviceName == 'ledGrn':
        actuator = ledGrn

    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)

    ledRedSts = GPIO.input(ledRed)
    ledGrnSts = GPIO.input(ledGrn)

    templateData = {
        'ledRed': ledRedSts,
        'ledGrn': ledGrnSts,
    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
