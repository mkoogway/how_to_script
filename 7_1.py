import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
comp = 4
troyka = 17
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)
number = [0] * 8


#def Tr_v():
    


def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

def adc():
    for i in range(256):
        GPIO.output(dac, dec2bin(int(i)))
        time.sleep(0.001)
        if 1 - GPIO.input(comp):
            GPIO.output(dac, 0)
            return i
    return 0


try:
    meas = []
    period = 0.01
    start = time.time()
    # подать на тройку 3.3В
    while напряжение на конденсаторе < 0.97*3.3:
        meas.append(напряжение на конденсаторе)
        time.sleep(period)
    # подать на тройку 0В
    while напряжение на конденсаторе > 0.02*3.3:
        meas.append(напряжение на конденсаторе)
        time.sleep(period)
    end = time.time()

    meas = [str(item) for item in meas]

    with open("data.txt", "w") as outfile:
        outfile.write("./".join(meas))

    with open("settings.txt", "w") as setfile:
        setfile.write(str())
        setfile.write(str())

    print(f"Duration: {end-start}\n")
    print(f"Period: {period}\n")
    print(f"Descr: {discrt}\n")
    print(f"Kvant: {kvant}\n")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()