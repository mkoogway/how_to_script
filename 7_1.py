#import RPi.GPIO as GPIO
import time

dac = [10, 9, 11, 5, 6, 13, 19, 26][::-1]
leds = [24, 25, 8, 7, 12, 16, 20, 21]
comp = 4
troyka = 17

"""GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)
GPIO.setup(comp, GPIO.IN)
GPIO.setup(troyka, GPIO.OUT, initial=1)"""
number = [0] * 8


def tr_v():
    return GPIO.input(comp)


def dec2bin(val):
    return [int(bit) for bit in format(val, "b").zfill(8)]

def binShow(val):
    GPIO.output(leds, dec2bin(val))

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

    #GPIO.output(troyka, 1)
    #v = tr_v()
    v = 0
    while v < 0.97*3.3:
        meas.append(v)
        #v = tr_v()
        v += 0.1
        time.sleep(period)

    #GPIO.output(troyka, 0)
    #v = tr_v()
    v = 3.3
    while v > 0.02*3.3:
        meas.append(v)
        #v = tr_v()
        v -= 0.1
        time.sleep(period)

    end = time.time()

    meas = [str(item) for item in meas]

    with open("data.txt", "w") as outfile:
        outfile.write("\n".join(meas))

    with open("settings.txt", "w") as setfile:
        setfile.write(str(1/period))
        setfile.write("\n")
        setfile.write(str("step"))

    print(f"Duration: {end-start}\n")
    print(f"Period: {period}\n")
    print(f"Descr: {1/period}\n")
    print(f"Kvant: ???\n")
    
finally:
    """GPIO.output(dac, 0)
    GPIO.cleanup()"""
