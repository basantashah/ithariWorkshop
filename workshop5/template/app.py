import RPi.GPIO as GPIO
from flask import Flask, render_template, request
app = Flask(__name__)
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# define the led pin you want to connect
ledRed = 8

# initialize GPIO status variables
ledRedSts = 0


# Define led pins as output
GPIO.setup(ledRed, GPIO.OUT)

# turn leds OFF
GPIO.output(ledRed, GPIO.LOW)


@app.route("/")
def index():
    # Read Sensors Status
    ledRedSts = GPIO.input(ledRed)

    templateData = {
        'title': 'GPIO output Status!',
        'ledRed': ledRedSts,

    }
    return render_template('index.html', **templateData)


@app.route("/<deviceName>/<action>")
def action(deviceName, action):
    if deviceName == 'ledRed':
        actuator = ledRed

    if action == "on":
        GPIO.output(actuator, GPIO.HIGH)
    if action == "off":
        GPIO.output(actuator, GPIO.LOW)

    ledRedSts = GPIO.input(ledRed)

    templateData = {
        'ledRed': ledRedSts,

    }
    return render_template('index.html', **templateData)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
