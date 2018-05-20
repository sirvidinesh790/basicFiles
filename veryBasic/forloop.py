"""
for (i = 0; i < 20; i++){
	cout>>i;
}

"""
li = []


for i in range(20):
	print i


for i in range(20,100,5):
	print i


name = "Prashant"


for l in name:
	print l

students = [ ["pra","sha","nt"], ["ti","wari","shivay"], ["namah","hjh"], ["wgek"] ]


for s in students:
	print s

students = [ ["pra","sha","nt"], ["ti","wari","shivay"], ["namah","hjh"], ["wgek"] ]

for l in students:
	for t in l:
		for r in t:
			print r
	print " Inner List Ends"
print "Outer List Ends"



for l in students:
	for i, name in enumerate(l):
		print str(i) + " : " + name
		#print "..................."
	print "List Ends"
print "All List Ends"



students = [ ["prashant","mango","Elex"], ["sagar","grapes","cs"], ["divyam","mango","ec"] ]


for l in students:
    print l[0] + " Likes " + l[1] + " And is in " + l[2] + " Branch"




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


l = []
a = ""

while True:
	a = raw_input("Enter name to enter into list : ")
	if( a == ""):
		break
	l.append(a)

print l
