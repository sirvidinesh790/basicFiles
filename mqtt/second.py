import paho.mqtt.subscribe as subscribe
from sys import stdout
from time import sleep
i = 0
while True:
	i = i + 1
	msg = subscribe.simple("paho", hostname="broker.shiftr.io",auth={'password':'SomeWhereOverTheRainbows','username':'newpiforclass'})
	stdout.write("\r"+"%s : %s" % (msg.topic, msg.payload))
	stdout.flush()
	sleep(.01)
