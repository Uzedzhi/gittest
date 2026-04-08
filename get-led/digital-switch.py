import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(26, GPIO.OUT)
GPIO.setup(13, GPIO.IN)

state = 0
while True:
    if GPIO.input(13):
        state = not state
        GPIO.output(26, state)
        time.sleep(0.2)