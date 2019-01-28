from tkinter import *

def btnclick(number):
    global operator
    operator = operator + str(number)
    text_Input.set(operator)

def btnclear():
    global operator
    operator =""
    text_Input.set("")

def btnEquals():
    global operator
    sumup = str(eval(operator))
    text_Input.set(sumup)
    operator = ""

    

cal =Tk()
cal.title("calculator")
operator=""
text_Input = StringVar()

txtdisplay = Entry(cal,font=("arial" ,20 , "bold" ), textvariable= text_Input, bd= 30 ,insertwidth=3,bg = "yellow" ,justify ="right" ).grid(columnspan=4)




button7 = Button(cal,padx=16 , pady=16, bd=8 , fg= "black",font=("arial" ,20, "bold" ), text = "7",command = lambda:btnclick(7))
button7.grid(row=1, column=0)

button8= Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "8",command = lambda:btnclick(8))
button8.grid(row=1, column=1)

button9 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "9",command = lambda:btnclick(9))
button9.grid(row=1, column=2)

buttonadd = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "+",command = lambda:btnclick("+"))
buttonadd.grid(row=1, column=3)

# secong row.............. 


button4 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "4",command = lambda:btnclick(4))
button4.grid(row=2, column=0)

button5 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "5",command = lambda:btnclick(5))
button5.grid(row=2, column=1)

button6= Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "6",command = lambda:btnclick(6))
button6.grid(row=2, column=2)

buttonsub = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "-",command = lambda:btnclick("-"))
buttonsub.grid(row=2, column=3)

# third row............

button1 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "1",command = lambda:btnclick(1))
button1.grid(row=3, column=0)

button2 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "2",command = lambda:btnclick(2))
button2.grid(row=3, column=1)

button3 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "3",command = lambda:btnclick(3))
button3.grid(row=3, column=2)

buttonmulti = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "*",command = lambda:btnclick("*"))
buttonmulti.grid(row=3, column=3)

# fourth row................

button0 = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "0",command = lambda:btnclick(0))
button0.grid(row=4, column=0)

buttonclr = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "c",command = btnclear)
buttonclr.grid(row=4, column=1)

buttonequ = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "=",command = btnEquals)
buttonequ.grid(row=4, column=2)

buttondiv = Button(cal,padx = 16 , pady =16 ,bd=8, fg= "black",font=("arial" ,20 , "bold" ), text = "/",command = lambda:btnclick("/"))
buttondiv.grid(row=4, column=3)


cal.mainloop()

