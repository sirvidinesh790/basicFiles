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
a = 456
############################
while(a > 50):
	print 1
	print 2
	print 3
print 4
print 5
############################


#############################
while(condition):
	print 1
	print 2
	if(anotherCondition):
		break
	print 3
############################



while(condition or anotherCondition):
	print 1
	print 2
	
	print 3


#############################
while(condition):
	print 1
	print 2
	if(anotherCondition):
		continue
	print 3
	print 4
##############################

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






