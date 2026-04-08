import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

leds = [24, 22, 23, 27, 17, 25, 12, 16][::-1]
GPIO.setup(leds, GPIO.OUT)
GPIO.output(leds, 0)

GPIO.setup(9, GPIO.IN)
GPIO.setup(10, GPIO.IN)

light_time = 0.1

def dec2bin(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]
num = 0
while True:
    inputup = GPIO.input(9)
    inputdown = GPIO.input(10)
    if (inputup and inputdown):
        num = 127
    elif (inputup):
        if num == 127:
            num = 0
        else:
            num += 1
    elif (inputdown):
        if num == 0:
            num = 127
        else:
            num -= 1
    GPIO.output(leds, dec2bin(num))
    time.sleep(light_time)
