from basic_functions import *
from nplists import *




def oneBYone():
    while True:
        for i in range(12):
            s = 4.8
            for j in range(10000):
                np[i] = hsv_to_rgb(colors12[i],100,sine(s))
                np.write()
                s += 0.01
                if sine(s) < 0.1:
                        reset()
                        break
            reset()
        


def siren1():
    time = 0
    while time < 100:
        for i in range(8):
            np[i] = hsv_to_rgb(colors["blue"],100,100)
        np.write()
        sleep(0.5)
        reset()
        for i in range(8,16):
            np[i] = hsv_to_rgb(0,100,100)
        np.write()
        sleep(0.5)
        reset()
        time += 15

def siren2():
    def wave(i):
        if i < 9:
            return (i/8) * 100
        else:
            return (1 - (i/8)) * 100
    time  = 0
    while time < 100:
        for j in range(16):
            for i in range(16):
                np[(i + j) % 16] = hsv_to_rgb(70+(i/24),100, wave(i))
                np.write()
                sleep(0.01)
                time += 1
                reset()


def siren3():
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




while True:
    siren3()

