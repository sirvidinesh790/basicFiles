print "Hello World"

a = raw_input("Enter a : ")
b = raw_input("Enter b : ")
c = int(a) + int(b)

print "Sum is : " + str(c)

if(c > 100):
	print "Greater than 100"

	if(c > 200):
		print "Greater than 200"

elif(c > 50):
	print "Greater than 50"
else:
	print "Smaller than 50"


print "End of Programe"
