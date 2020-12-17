# Setup

from neopixel import NeoPixel as neopixel
from time import sleep
from machine import Pin as pin
from machine import ADC
from math import sin
from urandom import getrandbits


button = pin(4,pin.IN, pin.PULL_UP)
np = neopixel(pin(5),16, bpp=4)
adc = ADC(0)
button = pin(4,pin.IN, pin.PULL_UP)


colors = {
	"red":		0,
	"orange":		3,
	"yellow":		9,
	"lime":		21,
	"green":		32,
	"aqua":		37,
	"sky":		49,
	"blue":		64,
	"purple":		71,
	"violet":		77,
	"pink":		84,
	"fuschia":	98
}

colors12 = [99,7,16,24,32,41,49,57,69,77,86,92]


def checkButton():
    if button.value() == 0:
        return True

def randint(min, max):
    span = max - min + 1
    div = 0x3fffffff // span
    offset = getrandbits(30) // div
    val = min + offset
    return val

def sine(x):
    y = sin(x)
    y += 1
    y *= 50
    return y

def alog():
    s = adc.read()
    t = (s / 3) - 7
    v = round(t)
    if v < 0:
        v = 0
    if v > 100:
        v = 100
    return v

def wave(i):
    if i < 9:
        return (i/8) * 100
    else:
        return (1 - (i/8)) * 100
    time  = 0

def hsv_to_rgb(h, s, v):
    h, s, v = h/100, s/100, v/100
    w = int(v*255)
    if s == 0.0:
        s = 0.01
    i = int(h*6.0) # XXX assume int() truncates!
    f = (h*6.0) - i
    p = int((v*(1.0 - s))*255)
    q = int((v*(1.0 - s*f))*255)
    t = int((v*(1.0 - s*(1.0-f)))*255)
    i = i%6
    if i == 0:
        return (w, t, p, 0)
    if i == 1:
        return (q, w, p, 0)
    if i == 2:
        return (p, w, t, 0)
    if i == 3:
        return (p, q, w, 0)
    if i == 4:
        return (t, p, w, 0)
    if i == 5:
        return (w, p, q, 0)

def reset():
    for i in range(16):
        np[i] = (0,0,0,0)
    np.write()

def setAll(h,s,v):
    for i in range(16):
        np[i] = hsv_to_rgb(h,s,v)
    np.write()

def setHue(h):
    setAll(h,100,100)

def setColor(c):
    setHue(colors[c])

def setWhite(n):
    for i in range(16):
        w = int((255 * n) / 100)
        np[i] = (0,0,0,w)
    np.write()

def do_nothing():
    while True:
        if button.value() == 0:
            return
        else:
            reset()

def checkReloop():
    sleep(0.2)
    if checkButton():
        sleep(0.2)
        if checkButton():
            setHue(0)
            sleep(0.05)
            reset()
            setHue(0)
            for i in range(16):
                np[i] = hsv_to_rgb(0,0,0)
                np.write()
                sleep(0.05)
            while True:
                if checkButton():
                    sleep(0.2)
                    return True
