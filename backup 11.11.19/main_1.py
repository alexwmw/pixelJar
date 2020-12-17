
from basic_functions import *


# Main function

def cycle():
    while True:
        sleep(0.2)
        rainblend()
        sleep(0.2)
        singleSine()
        sleep(0.2)
        spinStrobe()
        sleep(0.2)
        Dance()
        sleep(0.2)
        #Thunder()
        #sleep(0.2)
        Spectrum()
        sleep(0.2)
        Sparkle()
        sleep(0.2)
        Calm()
        sleep(0.2)
        do_nothing()


# Light shows



def welcome():
        for i in range(16):
            #if i % 5 == 0:
            if i < 5:
                np[i] = (100,0,0,0)
                np.write()
                sleep(0.1)
            elif i < 11:
                np[i] = (0,100,0,0)
                np.write()
                sleep(0.1)
            elif i <16:
                np[i] = (0,0,100,0)
                np.write()
                sleep(0.1)
        for i in range (50):
            for j in range(16):
                k = 100-(i*2)
                np[j] = (k,k,k,k)
            np.write()
        reset()

def Sparkle():
    h = 0
    while True:
        for i in range (1,201):
            h += 0.5
            for j in range(16):
                np[j] = hsv_to_rgb(h,100,alog())
            if button.value() == 0:
                return
            np.write()
        h = 0
    reset()

def Thunder():
    h = 0
    while True:
        if button.value() == 0:
            return
        for i in range (1,501):
            if i <= 350:
                l = i-1
            else:
                l = i - 251
            h += 0.2
            for j in range(16):
                np[j] = hsv_to_rgb(h,100,thunder[l])
            if button.value() == 0:
                return
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
            if button.value() == 0:
                return
            np.write()
        h = 0
    reset()

def Dance():
    s = 0
    while True:
        if button.value() == 0:
            return
        s+= alog() / 100
        for j in range(16):
            np[j] = hsv_to_rgb((sin(s)+1)*50,100,100)
        if button.value() == 0:
            return
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
        if button.value() == 0:
            return
        np.write()
    reset()

def singleSine():
    run = 1
    while True:
        for i in range (50):
            if i % 6 == 0:
                hue = 0
                s = 4.8
                while True:
                    if button.value() == 0:
                        return
                    speed = alog()
                    if speed == 0:
                        speed = 1
                    s += speed / 100
                    if sine(s) < 0.1:
                        reset()
                        run += 1
                        break
                    if run % 3 == 0:
                        np[i % 16]       = hsv_to_rgb(hue,100,sine(s))
                        np[(i * 3) % 16] = hsv_to_rgb((hue + 66) % 100,100,sine(s))
                        np[(i + 7) % 16] = hsv_to_rgb((hue + 28) % 100,100,sine(s))
                        np[(i + 2) % 16] = hsv_to_rgb((hue + 33 + 10) % 100,100,sine(s))
                        np.write()
                    elif run % 3 == 1:
                        np[i % 16]       = hsv_to_rgb((hue + 7 * i) % 100,100,sine(s))
                        np[(i * 3) % 16] = hsv_to_rgb((hue + 66 + 20) % 100,100,sine(s))
                        #np[(i + 7) % 16] = hsv_to_rgb((hue + 33 + 17.5) % 100,100,sine(s))
                        np[(i + 2) % 16] = hsv_to_rgb((hue + 33 + 25) % 100,100,sine(s))
                        np.write()
                    elif run % 3 == 2:
                        np[(i * 3) % 16] = hsv_to_rgb((hue + 7 * i) % 100,100,sine(s))
                        #np[(i + 7) % 16] = hsv_to_rgb((hue + 33 + 17.5) % 100,100,sine(s))
                        np[(i + 2) % 16] = hsv_to_rgb((hue + 85) % 100,100,sine(s))
                        np.write()

def rainblend():
        while True:
            for color in range(12):
                for i in range(16):
                    np[i] = hsv_to_rgb(colors12[color],100,100)

                np.write()
                for i in range(100):
                    if button.value() == 0:
                        reset()
                        return
                    sleep(0.01)
                for i in range(1,8):
                    for j in range(16):
                        np[j] = hsv_to_rgb(colors12[color]+i,100,100)
                    if button.value() == 0:
                        reset()
                        return
                    np.write()
                    sleep(0.01)



def spinStrobe():
    def spin(color):
        for j in range(16):
            for i in range(16):
                np[(i + j) % 16] = hsv_to_rgb(color % 100,100, wave(i))
                if button.value() == 0:
                    return
                np.write()
                sleep(0.02)
                reset()
            for i in range(32):
                if i % 2 == 0:
                    np[15-(((i//2) + j) % 16)] = hsv_to_rgb(color+50 % 100,100, wave(i))
                    if button.value() == 0:
                        return
                    np.write()
                    sleep(0.01)
                    #reset()
                else:
                    reset()
                    sleep(0.01)
    while True:
        color_set = ["lime", "fuschia", "orange", "green", "purple"]
        for color in color_set:
            spin(colors[color])
        if button.value() == 0:
            return

welcome()
sleep(1)
cycle()
