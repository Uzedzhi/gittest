import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16][::-1]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)

light_time = 0.2

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]

while True:
    for i in leds:
        GPIO.output(i, 1)
        time.sleep(light_time)
        GPIO.output(i, 0)
    for i in reversed(leds[1:-1]):
        GPIO.output(i, 1)
        time.sleep(light_time)
        GPIO.output(i, 0)