import paho.mqtt.subscribe as subscribe
from sys import stdout
from time import sleep
while True:

	msg = subscribe.simple("new",
		hostname="broker.shiftr.io",
		#auth={'password':'SomeWhereOverTheRainbows','username':'newpiforclass'})
		auth={'password':'qweasdzxc',"username":"karishma"})
#print "Message is :::: " + msg.payload
	stdout.write("\r" +  msg.payload)
	stdout.flush()
	sleep(.01)
