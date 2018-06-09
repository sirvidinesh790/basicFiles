#!/usr/bin/python

import thread
import time
from sys import stdout
from datetime import datetime as dt
stdout.write("\n\n")
# Define a function for the thread
def print_time( threadName, delay):
   while True:
      if delay == 1:
         stdout.write("\033[F" + str(dt.now().second)+"\n")
         stdout.flush()
      if delay == 2:
         stdout.write("\033[F\033[F" + str(dt.now().minute) + "\n\n")
         stdout.flush()

# Create two threads as follows
try:
   thread.start_new_thread( print_time, ("Thread-1", 1, ) )
   thread.start_new_thread( print_time, ("Thread-2", 1, ) )
except:
   print "Error: unable to start thread"

while 1:
   pass
