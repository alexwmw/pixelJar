import socket
import network
from basic_functions import *
from lights_mode import welcome

sta_if = network.WLAN(network.STA_IF)
ip = sta_if.ifconfig()[0]


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 pixelJar</title> </head>
<center><h2>Modes Test</h2></center>
<center><h3>My IP address is: {code}</h3></center>
<form>
Buttons:
<button name="dance" value="ON" type="submit">Dance</button>
<button name="spinStrobe" value="ON" type="submit">Spinstrobe</button>
<button name="rainblend" value="ON" type="submit">Rainblend</button>
<button name="reset" value="ON" type="submit">Off</button>
<br><br>

</form>
</html>
""".format(code = ip)

#Shows

def Dance():
    s = 0
    if button.value() == 0:
        return
    s+= alog() / 100
    for j in range(16):
        np[j] = hsv_to_rgb((sin(s)+1)*50,100,100)
    if button.value() == 0:
        return
    np.write()

def rainblend():
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

def spinStrobe():
    while True:
        color_set = ["lime", "fuschia", "orange", "green", "purple"]
    for color in color_set:
        spin(colors[color])
    if button.value() == 0:
        return

#Setup PINS
#LED5 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s.bind(addr)
s.listen(5)
welcome()
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    spinStrobe_on = request.find('/?spinStrobe=ON')
    rainblend_on = request.find('/?rainblend=ON')
    dance_on = request.find('/?dance=ON')
    reset_on = request.find('/?reset=ON')

    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if spinStrobe_on == 6:
        spinStrobe()
    if rainblend_on == 6:
        rainblend()
    if dance_on == 6:
        Dance()
    if reset_on == 6:
        reset()
    response = html
    conn.send(response)
    conn.close()
