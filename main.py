from basic_functions import *
from lights import *

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



while True:
    welcome()
    sleep(0.2)
    cycle()
