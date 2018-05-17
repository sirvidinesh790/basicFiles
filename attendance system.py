from Tkinter import *
import xlwt,xlrd

def submit():
    roll=int(line_input.get())
    name=line_input2.get()
    print "submitted"
    """attendance=xlwt.Workbook()#
    sheet1=attendance.add_sheet("my_attendance_system")#
    cols=["roll no.","name"]
    sheet1.write(0,0,name)
    attendance.save("attend.xls")"""
    rb=xlwt.Workbook()
    sheet=rb.add_sheet("1")
    sheet.write(0,0,roll)
    sheet.write(0,1,name)
    rb.save("manish.xls")
    

    
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
