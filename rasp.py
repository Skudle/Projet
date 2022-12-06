from sense_hat import SenseHat
import time

s = SenseHat()
s.low_light = True

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def smiley_face():
    Y = yellow
    O = nothing
    logo = [
    O, O, Y, Y, Y, Y, O, O,
    O, Y, O, Y, Y, O, Y, O,
    Y, Y, O, Y, Y, O, Y, Y,
    Y, Y, O, Y, Y, O, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, O, Y, Y, Y, Y, O, Y,
    O, Y, O, O, O, O, Y, O,
    O, O, Y, Y, Y, Y, O, O,
    ]
    return logo

def sad_face():
    Y = yellow
    O = nothing
    logo = [
    O, O, Y, Y, Y, Y, O, O,
    O, Y, O, Y, Y, O, Y, O,
    Y, Y, O, Y, Y, O, Y, Y,
    Y, Y, O, Y, Y, O, Y, Y,
    Y, Y, Y, Y, Y, Y, Y, Y,
    Y, Y, Y, O, O, Y, Y, Y,
    O, Y, O, Y, Y, O, Y, O,
    O, O, Y, Y, Y, Y, O, O,
    ]
    return logo

def current_temp():
    sense = SenseHat()
    temp = sense.get_temperature_from_pressure()
    print("Temperature: %s C" % temp)
    return temp

def current_humidity():
    ense = SenseHat()
    humidity = sense.get_humidity()
    print("Humidity: %s %%rH" % humidity)
    return humidity

while True:
  if current_temp() >= 25 and current_temp() <=40:
    s.set_pixels(smiley_face())
  else:
    s.set_pixels(sad_face())
  time.sleep(1)