import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
phototrans = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(phototrans, GPIO.IN)

while True:
    state = (GPIO.input(phototrans))
    GPIO.output(led, state)
    time.sleep(0.5)