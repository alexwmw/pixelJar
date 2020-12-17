import socket
import network
from basic_functions import *

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
<button name="NP" value="ON" type="submit">NP ON</button>
<button name="NP" value="OFF" type="submit">NP OFF</button><br><br>
</form>
</html>
""".format(code = ip)

#Setup PINS
#LED5 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
addr = socket.getaddrinfo('0.0.0.0', 80)[0][-1]
s.bind(addr)
s.listen(5)
while True:
    print('waiting to accept...')
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    NPON = request.find('/?NP=ON')
    NPOFF = request.find('/?NP=OFF')
    print(NPON)
    #print("Data: " + str(LEDON0))
    #print("Data2: " + str(LEDOFF0))
    if NPON == 6:
        print('TURN NP ON')
        setAll(100,100,100)
    if NPOFF == 6:
        print('TURN NP OFF')
        reset()
    response = html
    conn.send(response)
    conn.close()
