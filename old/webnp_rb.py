import socket
import network
from basic_functions import *
from lights_mode import welcome

sta_if = network.WLAN(network.STA_IF)
ip = sta_if.ifconfig()[0]


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 np[0] ON/OFF</title> </head>
<center><h2>A simple webserver for np[0]</h2></center>
<center><h3>My IP address is: {code}</h3></center>
<form>
np:
<button name="RB" value="ON" type="submit">RB ON</button>
<button name="NP" value="OFF" type="submit">NP OFF</button><br><br>
</form>
</html>
""".format(code = ip)

#Setup PINS
#LED5 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
welcome()
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s.bind(addr)
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    RBON = request.find('/?RB=ON')
    NPOFF = request.find('/?NP=OFF')

    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if RBON == 6:
        for color in range(12):
            for i in range(16):
                np[i] = hsv_to_rgb(colors12[color],100,100)

            np.write()
            for i in range(100):
                if button.value() == 0:
                    reset()

                sleep(0.01)
            for i in range(1,8):
                for j in range(16):
                    np[j] = hsv_to_rgb(colors12[color]+i,100,100)
                if button.value() == 0:
                    reset()

                np.write()
                sleep(0.01)
    if NPOFF == 6:
        reset()
    response = html
    conn.send(response)
    conn.close()
