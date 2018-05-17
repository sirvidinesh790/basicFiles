from Tkinter import *
import xlwt,xlrd
from xlutils.copy import copy

def submit():
    roll=int(line_input.get())
    name=line_input2.get()
    print "submitted"#
       
        

    b1= xlrd.open_workbook('manish.xls', 'r')
    s1 = b1.sheet_by_index(0)

    rowx=s1.nrows
    colx=s1.ncols
    b2 = copy(b1)  # creates a writeable copy
    sheet1 = b2.get_sheet(0)  # get a first sheet
    for k in range(colx):
        sheet1.write(rowx,0,roll)
        sheet1.write(rowx,1,name)

    b2.save("manish.xls")
    
   
    

    
w1=Tk()
w1.title("attendance system")
w1.configure(bg="white")
w1.geometry("480x720")

line_print=Label(w1, width=20,text="enter your roll no.-")      
line_print.grid(column=0, row=0)

line_input=Entry(w1,text="eg 25",width=30,bg="silver")
line_input.grid(column=1,row=0)
line_input.focus()



line_print1=Label(w1,width=20, text="enter your name-")               #w1 = specifying window (optional), text = giving output or print data (optional)
line_print1.grid(column=0, row=2)

line_input2 = Entry(w1,width=30,bg="silver")
line_input2.grid(column=1,row=2)
#line_input2.focus()

btn = Button(w1, text="submit", bg = "silver", command=submit,width=10)      #creating button w1=window(optionL),text= replacement of print(optionL),
btn.grid(column=0, row=4) 






w1.mainloop()
