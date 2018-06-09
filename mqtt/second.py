import paho.mqtt.subscribe as subscribe
from time import sleep
i = 0
while True:
	i = i + 1
	msg = subscribe.simple("paho", hostname="broker.shiftr.io",auth={'password':'SomeWhereOverTheRainbows','username':'newpiforclass'})
	print msg.payload
	sleep(.01)
