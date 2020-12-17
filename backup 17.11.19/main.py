from basic_functions import *

# Main function

def cycle():
    while True:

        threeFlavours()
        if checkReloop():
            return

        colorFade()
        if checkReloop():
            return

        allColours()
        if checkReloop():
            return

        fastColours()
        if checkReloop():
            return

        spectrum()
        if checkReloop():
            return

        spinning()
        if checkReloop():
            return

        pulse()
        if checkReloop():
            return

        calm()
        if checkReloop():
            return

        do_nothing()
        sleep(0.2)


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

def calm():
    z = 0
    y = 0
    x = randint(0,999999)
    while True:
        if sine(y) > 0.1:
            for i in range(16):
                np[i] = hsv_to_rgb(sine(x),sine(z),sine(y))
                np.write()
        else:
            x = randint(0,999999)
            #z = randint(0,100)
        y += 0.04
        z += 0.033
        if checkButton():
            reset()
            return

def fastColours():
    s = 0
    while True:
        if checkButton():
            return
        s+= 0.05
        for j in range(16):
            np[j] = hsv_to_rgb((sin(s)+1)*50,100,100)
        if checkButton():
            return
        np.write()
    reset()

def pulse():
    run = 1
    while True:
        for i in range (50):
            if i % 6 == 0:
                hue = 0
                s = 4.8
                while True:
                    if checkButton():
                        return
                    #speed = alog()
                    speed = 4
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

def allColours():
        while True:
            for color in range(12):
                for i in range(16):
                    np[i] = hsv_to_rgb(colors12[color],100,100)

                np.write()
                for i in range(100):
                    if checkButton():
                        reset()
                        return
                    sleep(0.01)
                for i in range(1,8):
                    for j in range(16):
                        np[j] = hsv_to_rgb(colors12[color]+i,100,100)
                    if checkButton():
                        reset()
                        return
                    np.write()
                    sleep(0.01)

def spinning():
    def spin(color):
        for j in range(1):
            for i in range(160):
                k = color % 100
                np[(i + j) % 16] = hsv_to_rgb(k + i,100, wave(i))
                if checkButton():
                    return
                np.write()
                sleep(0.02)
                reset()
            #for i in range(100):
            #    if i % 2 == 0:
            #        np[15-(((i//2) + j) % 16)] = hsv_to_rgb(color+50 % 100,100, wave(i))
            #        if checkButton():
            #            return
            #        np.write()
            #        sleep(0.02)
            #        #reset()
            #    else:
            #        reset()
            #        sleep(0.05)
    while True:
        color_set = ["lime", "fuschia", "orange", "green", "purple"]
        for color in color_set:
            spin(colors[color])
        if checkButton():
            return

def colorFade():
    x = 0
    count = 0
    flag = False
    while True:
        if checkButton():
            reset()
            return
        if sine(x) < 0.015 or sine(x) > 99.985:
            flag = not flag
        if flag:
            setHue(sine(x))

        x += 0.001

def spectrum():
    def setSing(p,h):
        np[p] = hsv_to_rgb(h,100,100)
    b = 0
    while True:
        if checkButton():
            reset()
            return
        for i in range(16):
            setSing(i,b)
            np.write()
            if i < 8:
                b += 9
            else:
                b -= 8

def puppieColors():
    reset()
    h = 0
    while True:
        setHue(h)
        if button.value() == 1:
            continue
        while h < 25:
            h+=1
            setHue(h)
        if button.value() == 1:
            continue
        while h < 66:
            h+=1
            if h % 2 == 0:
                setHue(h)
        if checkButton():
            reset()
            return

def threeFlavours():
    while True:
        h = 0
        for i in range(200):
            setHue(h)
            if checkButton():
                reset()
                return
        for i in range(25):
            h+=1
            setHue(h)
            setHue(h)
            if checkButton():
                reset()
                return
        for i in range(200):
            setHue(h)
            if checkButton():
                reset()
                return
        for i in range(41):
            h+=1
            if h % 2 == 0:
                setHue(h)
                if checkButton():
                    reset()
                    return
        for i in range(200):
            setHue(h)
            if checkButton():
                reset()
                return
        while h < 100:
            h +=1
            setHue(h)
            if checkButton():
                reset()
                return



while True:
    welcome()
    sleep(0.2)
    cycle()
