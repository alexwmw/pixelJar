import socket
from basic_functions import *


#HTML to send to browsers
html = """<!DOCTYPE html>
<html>
<head> <title>ESP8266 np[0] ON/OFF</title> </head>
<center><h2>A simple webserver for np[0]</h2></center>
<center><h3>(for noobs to both the ESP8266 and Micropython)</h3></center>
<form>
np:
<button name="NP" value="ON" type="submit">NP ON</button>
<button name="NP" value="OFF" type="submit">NP OFF</button><br><br>
</form>
</html>
"""

#Setup PINS
#LED5 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
while True:
    conn, addr = s.accept()
    print("Got a connection from %s" % str(addr))
    request = conn.recv(1024)
    print("Content = %s" % str(request))
    request = str(request)
    NPON = request.find('/?NP=ON')
    NPOFF = request.find('/?NP=OFF')

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
