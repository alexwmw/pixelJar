# Setup

from neopixel import NeoPixel as neopixel
from time import sleep
from machine import Pin as pin
from machine import ADC
from math import sin

from nplists import thunder

np = neopixel(pin(5),16, bpp=4)
adc = ADC(0)

button = pin(4,pin.IN, pin.PULL_UP)



# Basic functions

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

def alog():
    s = adc.read()
    t = (s / 3) - 7
    v = round(t)
    if v < 0:
        v = 0
    if v > 100:
        v = 100
    return v

def alog2():
    s = adc.read()
    t = (s / 3) - 7
    v = round(t)
    if v < 0:
        v = 0
    if v > 100:
        v = 100
    return v / 100


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

def hsv_to_rgbw(h, s, v, o):
    o = int(o*2.55)
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
        return (w, t, p, o)
    if i == 1:
        return (q, w, p, o)
    if i == 2:
        return (p, w, t, o)
    if i == 3:
        return (p, q, w, o)
    if i == 4:
        return (t, p, w, o)
    if i == 5:
        return (w, p, q, o)

def reset():
    for i in range(16):
        np[i] = (0,0,0,0)
    np.write()

def setAll(h,s,v):
    for i in range(16):
        np[i] = hsv_to_rgb(h,s,v)
    np.write()


# Light shows

def analog_bright(n):
    h = 0
    for k in range(n):
        for i in range (1,201):
            h += 0.5
            for j in range(16):
                np[j] = hsv_to_rgb(h,100,alog())
            np.write()
        h = 0
    reset()


def Sparkle(n):
    h = 0
    for k in range(n):
        for i in range (1,201):
            h += 0.5
            for j in range(16):
                np[j] = hsv_to_rgb(h,100,alog())
            np.write()
        h = 0
    reset()


def Sparkle2(n):
    h = 0
    for k in range(n):
        for i in range (1,201):
            for j in range(16):
                h += 1
                np[j] = hsv_to_rgb(h,100,alog()*0.5)
            np.write()
        h = 0
    reset()




def Thunder(n):
    h = 0
    for k in range(n):
        for i in range (1,501):
            if i <= 350:
                l = i-1
            else:
                l = i - 251
            h += 0.2
            for j in range(16):
                np[j] = hsv_to_rgb(h,100,thunder[l])
            np.write()
        h = 0
    reset()

def Calm():
    h = 0
    s = 0
    while True:
        for i in range (1,1001):
            h += 0.1
            s+= 0.02
            for j in range(16):
                np[j] = hsv_to_rgb(h,100,(sin(s)+1)*50)
            np.write()
        h = 0
    reset()


def Dance():
    s = 0
    while True:
        s+= alog() / 100
        for j in range(16):
            np[j] = hsv_to_rgb((sin(s)+1)*50,100,100)
        np.write()
    reset()

def Spectrum():
    #
    while True:
        m = []
        for i in range(50):
            m.append(alog())
            avg = sum(m) / len(m)
        for j in range(16):
            np[j] = hsv_to_rgb(avg,100,100)
        np.write()
    reset()




def singleSine(n):
    mode = 1
    for j in range(n):
        for i in range (50):
            if i % 6 == 0:
                hue = 0
                s = 4.8
                while True:
                    speed = alog()
                    if speed == 0:
                        speed = 1
                    s += speed / 100
                    if sine(s) < 0.1:
                        reset()
                        mode += 1
                        break
                    if mode % 3 == 0:
                        np[i % 16]       = hsv_to_rgb(hue,100,sine(s))
                        np[(i * 3) % 16] = hsv_to_rgb((hue + 66) % 100,100,sine(s))
                        np[(i + 7) % 16] = hsv_to_rgb((hue + 28) % 100,100,sine(s))
                        np[(i + 2) % 16] = hsv_to_rgb((hue + 33 + 10) % 100,100,sine(s))
                        np.write()
                    elif mode % 3 == 1:
                        np[i % 16]       = hsv_to_rgb((hue + 7 * i) % 100,100,sine(s))
                        np[(i * 3) % 16] = hsv_to_rgb((hue + 66 + 20) % 100,100,sine(s))
                        #np[(i + 7) % 16] = hsv_to_rgb((hue + 33 + 17.5) % 100,100,sine(s))
                        np[(i + 2) % 16] = hsv_to_rgb((hue + 33 + 25) % 100,100,sine(s))
                        np.write()
                    elif mode % 3 == 2:
                        np[(i * 3) % 16] = hsv_to_rgb((hue + 7 * i) % 100,100,sine(s))
                        #np[(i + 7) % 16] = hsv_to_rgb((hue + 33 + 17.5) % 100,100,sine(s))
                        np[(i + 2) % 16] = hsv_to_rgb((hue + 85) % 100,100,sine(s))
                        np.write()
                    print(sine(s))



while True:
    if button.value() ==0:
        print('ok!')
        break
