a="ANNAESSACAR"
i = 0
length = len(a)

while (i<length/2+1):
        print " "*i + a[i]+ " "*(length-i*2) + a[length-i-1]
        i=i+1
while (i>-1):
        print " "*i + a[i]+ " "*(length-i*2) + a[length-i-1]
        i=i-1
       
    
