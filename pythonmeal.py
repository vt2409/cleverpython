''''online booing meal
and you can store the all information in file              '''

                                                     
from tkinter import *
cal = Tk()
cal.title("cleveraadi mile")
cal.geometry("450x350")

def aadi():
	print("\t\twait a minute")
	print(f'{entryname.get(),entryphone.get(),entrygender.get(),entryemergrency.get(),entrypaymentmode.get(),foodservicevalue.get()}')

	
        with open("records.txt","w") as f :
        f.write(f"{entryname.get(),entryphone.get(),entrygender.get(),entryemergrency.get(),entrypaymentmode.get(),foodservicevalue.get()}")



label1=Label(cal,text="WELCOME TO THE CLEVER_AADI MEAL",font=('comicsansms',13,'bold'),padx=5)
label1.grid(row=0,column=3)
name=Label(cal,text="Name")
phone=Label(cal,text="Phone")
gender=Label(cal,text="Gender")
emergency=Label(cal,text="Emergency")
paymentmode=Label(cal,text="Payment mode")

name.grid(row=1,column=2)
phone.grid(row=2,column=2)
gender.grid(row=3,column=2)
emergency.grid(row=4,column=2)
paymentmode.grid(row=5,column=2)

entryname=StringVar()
entryphone=StringVar()
entrygender=StringVar()
entryemergrency=StringVar()
entrypaymentmode=StringVar()
foodservicevalue=IntVar()

nameentry=Entry(cal,textvariable=entryname)
phoneentry=Entry(cal,textvariable=entryphone)
genderentry=Entry(cal,textvariable=entrygender)
emergencyentry=Entry(cal,textvariable=entryemergrency)
paymententry=Entry(cal,textvariable=entrypaymentmode)

nameentry.grid(row=1,column=3)
phoneentry.grid(row=2,column=3)
genderentry.grid(row=3,column=3)
emergencyentry.grid(row=4,column=3)
paymententry.grid(row=5,column=3)
#checkbutton

foodservice= Checkbutton(text="Want to prebook your meal",variable=foodservicevalue)
foodservice.grid(row=6,column=3)

button1=Button(cal,text="Submit",font=('arial',13,'bold'),command=aadi).grid(row=7,column=3)


cal.mainloop()

