#Python uses Indentation Instead of Brackets for specifying a block of code
#We use ':' to tell python that we are going to use indentation now for 
#specific block of code to be under particular statement like if/elif/else/whie/for and many other

#input vs raw_input ?
#print "a string like this"
#print variable
#print variable1, variable2, variable3

##########################################################################

#while loop runs the block of code until a specific condition is False.
#while can be used in many intelligent ways, code more and more to find out how

a = 400
b = 0
############################
while(a > b):
	print 1
	b = input("Enter value of b : ")
	print 2
	print 3
print 4
print 5
############################

a = 1000
#############################
while(a > b):
	print 1
	b = input("b : ")
	print 2
	if(b == 8):
		break
	print 3
############################


b = 600

while( (b > 500) or (b < 100) ):
	print 1
	print 2
	b = input("Enter b : ")
	print 3

"""
#############################
while(condition):
	print 1
	print 2
	if(anotherCondition):
		continue
	print 3
	print 4
##############################
"""

#A string is a list or an array of characters
mySentance = "this line will be printed until the letter z is encounter"
#mySentence[0] will return "t"
#mySentance[5] will return ?


is_Z_encountered = False
i = 0

while(is_Z_encountered != True):
	print mySentance[i]
	if(mySentance[i] == 'z'):
		is_Z_encountered = True #break
	i = i + 1

#Use while loop to run a block over and over on our demand, if yes run the while block again,
#if anything else, break out of while loop


wish  = "y"

while(wish == "y"):
	print "This loop will continue untill my wish is not y"
	wish = raw_input("What is your wish ? ")


a = 100
b = 1

while(a > b):
	print 1
	b = raw_input("b : ") # b = int(raw_input("b : "))
	b = int(b)
	print 2
	if(b == 0):
		break
	print 3


