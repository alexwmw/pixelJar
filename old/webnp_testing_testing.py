import socket
import network
from basic_functions import *

sta_if = network.WLAN(network.STA_IF)
ip = sta_if.ifconfig()[0]


#HTML to send to browsers
html = """<!DOCTYPE html>

<head>

	<style>
	body{
		margin: 30pt;
		padding: 0;

		color: #333;
		/*background-color: #eee;*/

	}

		h1, h2, h3, h4, h5, h6{
			font-weight: 200;
		}

		h1{
			text-align: center;

			font-size: 50px;
			padding-bottom: 10px;
			border-bottom: 2px solid #2fcc71;
			max-width: 40%;
			margin: 20px auto;
		}







	</style>
</head>
<body>

	<div class="container">
			<h1>pixel<b>Jar</b></h1>
			<center><h3>a simple control interface</h3></center>
			<form class="form cf">
				<section class="plan cf">
					<h2>Mode select:</h2>

					<input type="radio" name="radio1" id="One" 	value="One" checked>
								<label class="One-label four col"				for="One"								>One</label>
					<input type="radio" name="radio1" id="Two" 		value="Two" >
								<label class="Two-label four col"					for="Two"							>Two</label>
					<input type="radio" name="radio1" id="Three" 	value="Three">
								<label class="Three-label four col"				for="Three"						>Three</label>
					<input type="radio" name="radio1" id="Four" 		value="Four">
								<label class="Four-label four col"					for="Four"					>Four</label>
	        <input type="radio" name="radio1" id="Five" 		value="Five">
								<label class="Five-label four col"					for="Five"					>Five</label>
					<input type="radio" name="radio1" id="Six" 	value="Six">
								<label class="Six-label four col"				for="Six"								>Six</label>
	      </section>

				<input class="submit" type="submit" value="Submit">
			</form>
		</div>




</body>



"""

#Setup PINS
#LED5 = machine.Pin(5, machine.Pin.OUT)

#Setup Socket WebServer
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
