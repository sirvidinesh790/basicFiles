# We open a file like below, with two arguments,
#1ist is the file name or address of the file
#second is 'r', 'w', 'a', 'r+' and more
file = open("testFile.txt","w")

#We now write to a file giving it an argument of
#strings to be writtten
file.write("Hello World , this is my first line")

#Point to remember here is that with 'write' function
#Cursor for writing is always set at the start of the file,
#and after finishing the writing of the string
#it stops and stays at the location of the end of the string

#we write another string to append to the string
#as our cursor is at the end of the string previously written
#writing further will append the string for this opened file
#session only, after clossing and reopening the file, cursor 
#will reset it self to start
file.write("Another Hello from me, but with a new line \n")
file.write("Succesfully placed a new line now")

#for further use of the file, and to clear
#the buffer, we close the file after our work
#this clears the resources for us, and also freeing
#other programms for editing or using that file
file.close()


#Now we see an example of Appending to a file
#As always we open and close the file
#with our work  sandwitched in between
file = open("testFile.txt","a")

file.write("\nAnother Appended Hello")

file.close()

#now an another way to open and close
#this is a safer method, coz it closes our file after
#processing the file automatically
with open("newFile.txt",'a') as f:
	f.write("Some String for demo purpose\n")
	f.write("Another line for demo again\n")

#now let's use a for loop with file to read lines
#as we know already, for loop can be used to iterrate
#over any elements(be it of list, strings, tuples, dict)
with open("students.txt",'r') as f:
	for a_single_line in f:
		print "Name : " + a_single_line
		#print "Name : " + a_single_line.strip('\n')
print "All names printed"
print ".............................................................."


#take input from a file(all names in new line) and make a list
name_list = [] # declaring an empty list
with open("students.txt",'r') as f:
	for line in f:
		name_list.append(line)
		#name_list.append(line.strip('\n'))
print name_list

#take input from a file(all names comma seperated) and make a list
#easy task, have performed previously,

#another way to write multiple lines from a list
with open("multiLineFromList.txt",'w') as f:
	f.writelines(name_list)







