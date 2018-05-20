#String is an array of a character data type
#String  in itself holds many functions or methods
#which we would be experimenting  further in class

name = "Prashant Tiwari"


#in strings we access it's elements(i.e characters at different location)
#by many methods involving the most common INDEXING
#we access an elemenet of a string as:

print name[3] # this prints 's', 4th element from start,

#be informed that indexing in python starts from 0,
#so first elemennt is 0 index, 4th element is 3 index

#python supports NEGETIVE INDEXING too
print name[-3] #this prints 'a', the third element from last



#now comming to SLICING,
#slicing is when we need two or more elements from a list,
#or in string's case, we want characters
#so herein we declare two things, [indexToStart:indexToStopBefore]
print name[2:5] # this prints "ash"

#we did not provide any start and stopBefore so it prints all characters
print name[:]


#this in the same way can be understood
print name[3:]


#STEPPING with SLICING
#we can provide strings to take twwo steps instead of one,
#stepping with 2 skips one elemeennts each time
print name[2:13:2] # this prints  "ahn Tw"
print name[3:9]

