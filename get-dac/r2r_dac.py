import RPi.GPIO as GPIO

class R2R_DAC:
    def __init__(self, GPIOpins, MaxVoltage, verbose=False):
        self.GPIOpins = GPIOpins
        self.MaxVoltage = MaxVoltage
        self.verbose = verbose
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.GPIOpins, GPIO.OUT, initial=0)
    
    def deinit(self):
        GPIO.output(self.GPIOpins, 0)
        GPIO.cleanup()
    
    def voltage_to_number(self, voltage):
        if not (0.0 <= voltage <= self.MaxVoltage):
            print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {self.MaxVoltage:.2f} B)")
            print("устанавливаем 0.0 В")
            return 0
        return int(voltage / self.MaxVoltage * 255)

    def dec2bin(self, num):
        return [bit for bit in bin(num)[2:].zfill(8)];

    def float_to_dac(self, number):
        number = self.voltage_to_number(number)
        BinNum = self.dec2bin(number)
        print(f"число на вход ЦАП: {number}, биты: {BinNum}")
        for i in range(len(self.GPIOpins)):
            GPIO.output(int(self.GPIOpins[i]), int(BinNum[i]))



if __name__ == "__main__":
    try:
        dac = R2R_DAC([16, 20, 21, 25, 26, 17, 27, 22], 3.3, True)

        while True:
            try:
                voltage = float(input("введите напряжение в Вольтах: "))
                dac.float_to_dac(voltage)

            except ValueError:
                print("вы ввели не число. Попробуйте еще раз")
    finally:
        dac.deinit()