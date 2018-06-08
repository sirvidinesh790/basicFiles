def a_method(a,b,*c,**de ):
	print "sum of a and b : " + str(a + b)
	sum = 0
	for i in c:
		sum  = sum + i
	print "sum of all 'c's : " + str(sum)

	for key, value in de.items():
		print key + " : " + value

a_method(1,2,1,2,3,4,5,6,7,8,9,fruit="Mango",drink="juice",school="gurukul")
