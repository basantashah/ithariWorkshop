from csv import writer
from sense_hat import SenseHat
sense = SenseHat()

# while True:

#   # Take readings from all three sensors
#   t = sense.get_temperature()
#   p = sense.get_pressure()
#   h = sense.get_humidity()

#   t = round(t, 1)
#   p = round(p, 1)
#   h = round(h, 1)


def getTempHum():
    sense_data = []
    sense_data.append(sense.get_temperature())
    sense_data.append(sense.get_pressure())
    sense_data.append(sense.get_humidity())

    return sense_data


with open('data.csv', 'w', newline='') as f:
    data_writer = writer(f)

    while True:
        data = getTempHum()
        data_writer.writerow(data)
