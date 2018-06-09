import paho.mqtt.publish as publish
import paho.mqtt.subscribe as subscribe
from sys import stdout
from time import sleep
import thread

i = 0

person_to = raw_input("Enter person to contact : ")
person_from = raw_input("Enter your name : ")

def listener(a,b):
	while True:
		messageFrom = subscribe.simple(person_to + "/" + person_from, hostname="broker.shiftr.io",auth={'password':'SomeWhereOverTheRainbows','username':'newpiforclass'})
		#print messageFrom.payload
		stdout.write("\r" + messageFrom.payload  + " "*len(person_from) + "\n")
		stdout.write(person_from + " : ")
		stdout.flush()
try:
	thread.start_new_thread( listener, ("1","2"))
except Exception as ex:
	print ex

while True:

	messageTo = raw_input(person_from + " : ")
	publish.single(person_from + "/" + person_to, messageTo, hostname="broker.shiftr.io",auth = {'username':"newpiforclass", 'password':"SomeWhereOverTheRainbows"})
