import RPi.GPIO as GPIO

GPIOpins = [16, 20, 21, 25, 26, 17, 27, 22]

GPIO.setmode(GPIO.BCM)
GPIO.setup(GPIOpins, GPIO.OUT)

MaxVoltage = 3.3
def voltage_to_number(voltage):
    if not (0.0 <= voltage <= MaxVoltage):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - {MaxVoltage:.2f} B)")
        print("устанавливаем 0.0 В")
        return 0
    return int(voltage / MaxVoltage * 255)

def dec2bin(num):
    return [bit for bit in bin(num)[2:].zfill(8)];

def number_to_dac(number):
    BinNum = dec2bin(number)
    print(f"число на вход ЦАП: {number}, биты: {BinNum}")
    for i in range(len(GPIOpins)):
        GPIO.output(int(GPIOpins[i]), int(BinNum[i]))

try:
    while True:
        try:
            voltage = float(input("введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            number_to_dac(number)
        except ValueError:
            print("Вы ввели не число. Попробуйте еще раз\n")
finally:
    GPIO.output(GPIOpins, 0)
    GPIO.cleanup()