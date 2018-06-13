#pip install paho-mqtt
import paho.mqtt.publish as publish
from time import sleep
i = 0
while True:
#	sleep(1)
	i = i + 1
	publish.single(topic="new",
		payload="current counter is : " + str(i),
		hostname="broker.shiftr.io",
		#auth = {'username':"newpiforclass", 'password':"SomeWhereOverTheRainbows"})
		auth = {'username':"karishma","password":'qweasdzxc'})
