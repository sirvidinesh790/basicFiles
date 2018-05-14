print "Welcome"
print ""
a = 7
b = 6

if (a > b):
	print "1"
	print "2"
elif (a < b):
	print "9"
else:
	print "5"
print "3"
print "4"


check = 'y'
while(check == 'y'):
      a =  input("enter value")
      b =  raw_input("enter operator")
      c =  input("enter value")
      if(b == '+'):
           d = a + c
           print d
      elif(b == '-'):
           d = a - c
           print d
      check = raw_input("y / n\n")
      if(check == n):
           break
