import RPi.GPIO as GPIO

class PWM_DAC:
    def __init__(self, GPIOpin, PWMfrequency, MaxVoltage, verbose=False):
        self.GPIOpin = GPIOpin
        self.MaxVoltage = MaxVoltage
        self.PWMfrequency = PWMfrequency
        self.verbose = verbose
        self.pwn = 0.0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOpin, GPIO.OUT, initial=0)
    
    def deinit(self):
        self.pwn.ChangeDutyCycle(0.0)
        self.pwn.stop()
        GPIO.output(self.GPIOpin, 0)
        GPIO.cleanup()

    def set_voltage(self, number):
        if number < 0.0:
            number = 0.0
        if number > self.MaxVoltage:
            number = self.MaxVoltage

        if self.pwn == 0.0:
            self.pwn = GPIO.PWM(self.GPIOpin, self.PWMfrequency)
            self.pwn.start(0.0)

        self.pwn.ChangeDutyCycle((number / self.MaxVoltage) * 100)
if __name__ == "__main__":
    try:
        dac = PWM_DAC(12, 500, 3.3, True);

        while True:
            try:
                voltage = float(input("введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)

            except ValueError:
                print("вы ввели не число. Попробуйте еще раз")
    finally:
        dac.deinit()