#list is a collection of data type enumerated by index startinng from 0
#unlike in c / c++, python supports lists with any kinds of data type
#list can have a list inside of it,
l = [34, "prashant", 56.78, 45, ["tiwari", 79], 56]

students = ["prashant", "tiwari", "sagar", "mohit", "saurav", "gaurav", "manish", "manoj"]
print l[-2][1]


print "..................................."



for val in students:
	val = val.upper()
	print val