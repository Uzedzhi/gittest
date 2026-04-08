import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

led = 26
phototrans = 6

GPIO.setup(led, GPIO.OUT)
GPIO.setup(phototrans, GPIO.IN)

pwn = GPIO.PWM(led, 200)
duty = 0.0
pwn.start(duty)

while True:
    pwn.ChangeDutyCycle(duty)
    time.sleep(0.05)

    duty += 1
    if duty > 50:
        duty = 0.0