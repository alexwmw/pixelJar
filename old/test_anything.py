import network
sta_if = network.WLAN(network.STA_IF)
ip = sta_if.ifconfig()[0]

print(ip)
