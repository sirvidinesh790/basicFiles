

for i in range(10):
	print i

name = "Prashant"

for letter in name:
	print letter

l = [1,2,3,"prashant",5,6,7.78,8,9,89]

f = l[3]

print l[6]

students = [ ["pra","sha","nt"], ["ti","wari","shivay"], ["namah","hjh"], ["wgek"] ]

"""

for s in students:
	print s

for l in students:
	for t in l:
		for r in t:
			print r
	print " Inner List Ends"
print "All List Ends"

"""

for l in students:
	for i, name in enumerate(l):
		print str(i) + " : " + name
		#print "..................."
	print "List Ends"
print "All List Ends"






students = [ ["prashant","mango","Elex"], ["sagar","grapes","cs"], ["divyam","mango","ec"] ]


for list in students:
    print list[0] + " : " + list[1] + " : " + list[2]




students = []

for i in range(5):
	s=raw_input("enter str:")
	s=students.append(s)
print students
print "list Ends"	

























for i in range(5): #for(i = 0;i<=5;i++){}
	s = raw_input()
	s =students.append(s)
print students

#Append into names into a list inside a while loop,
#taking input from user, until 'n' is inputted