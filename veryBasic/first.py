"""
print "Welcome"
print ""

a = input("Enter a :")
b = input("Enter b :")

c = a + b
print c


a = raw_input("Enter a : ")
b = raw_input("Enter b : ")
print a + b

#raw_input() always inputs string, raw_input is always safer to
#use than input(), if taking number or an integer from a
#raw_input() always remember to cast it into an integer like this :
# int(raw_input)

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
"""

print("welcome")
print""
a = input(" enter a")
b = input(" enter b")
c=a*b
print "multi is : " + str(c)
d=a-b
print "sub is : " +str(c)
e=a+b
print "sum is :"  +str(c)
f=(2*a)+5*b
print "fun is :"  +str(f)