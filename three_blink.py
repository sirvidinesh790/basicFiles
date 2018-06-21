"""
pins = [18,23,24,25,2,4]
from time import sleep
for pin in pins:
	io.setup(pin,io.OUT)

i = 0
c = 1
status = True
while True:
	io.output(pin[i],status)
	sleep(.2)
	i = i + c
	if ( i > (len(pins) - 2) ) or (i < 1):
		c = 0 -c
		status = not status
"""
from time import sleep
i, c, status = 0, 1, True
while True:
	sleep(.4)
	i = i + c
	if(i > 9) or (i < 1):
		c = 0 - c
		status = not status
	print i,status
