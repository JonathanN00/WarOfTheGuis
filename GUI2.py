import tkinter
jony = tkinter.Tk()

home = tkinter.Frame (jony, bg = "Sky Blue", height=600,width=400)
home.grid_propagate(False)
home.grid(row=0,column=0,sticky="nsew")

home.tkraise()
num1=0
num2=0
num3=0
num4=0
num5=0
num6=0

def enter7():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "7")

def enter8():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "8")

def enter9():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "9")

def enter4():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "4")

def enter5():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "5")

def enter6():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "6")

def enter1():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "1")

def enter2():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "2")

def enter3():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "3")

def enter0():
	Entries = Entry.get()
	Entry.configure(text =Entries +  "0")

def add():
	plus.configure(highlightbackground="Red")
	num1 = int(Entry.get())
	Entry.configure(text="")
	num2 = int(Entry.get())

def answer():
	num3 = num1 + num2
	Entry.configure(text = num3)




Entry = tkinter.Entry(home)
Entry.grid(row=0,column=0,columnspan=3,sticky="nsew")
number7 = tkinter.Button(home,text="7",highlightbackground="#ba7c14",width=5,command = enter7,font = ("Comic Sans MS",24))
number7.grid(row=2,column=0,sticky="nsew")
number8 = tkinter.Button(home,text="8",highlightbackground="#ba7c14",command = enter8,font = ("Comic Sans MS",24))
number8.grid(row=2,column=1,sticky="nsew")
number9 = tkinter.Button(home,text="9",highlightbackground="#ba7c14",command = enter9,font = ("Comic Sans MS",24))
number9.grid(row=2,column=2,sticky="nsew")
number4 = tkinter.Button(home,text="4",highlightbackground="#ba7c14",command = enter4,font = ("Comic Sans MS",24))
number4.grid(row=3,column=0,sticky="nsew")
number5 = tkinter.Button(home,text="5",highlightbackground="#ba7c14",command = enter5,font = ("Comic Sans MS",24))
number5.grid(row=3,column=1,sticky="nsew")
number6 = tkinter.Button(home,text="6",highlightbackground="#ba7c14",command = enter6,width=5,font = ("Comic Sans MS",24))
number6.grid(row=3,column=2,sticky="nsew")
number1 = tkinter.Button(home,text="1",highlightbackground="#ba7c14",command = enter1,font = ("Comic Sans MS",24))
number1.grid(row=4,column=0,sticky="nsew")
number2 = tkinter.Button(home,text="2",highlightbackground="#ba7c14",width=5,command = enter2,font = ("Comic Sans MS",24))
number2.grid(row=4,column=1,sticky="nsew")
number3 = tkinter.Button(home,text="3",highlightbackground="#ba7c14",command = enter3,font = ("Comic Sans MS",24))
number3.grid(row=4,column=2,sticky="nsew")
number0 = tkinter.Button(home, text="0",width=3,command = enter0,font=("Comic Sans MS",24))
number0.grid(row=5,column=0,columnspan=2,sticky="nsew")
decimal = tkinter.Button(home, text=".",highlightbackground="#ba7c14",font= ("Comic Sans MS",24))
decimal.grid(row=5,column=2,sticky="nsew")
plus = tkinter.Button(home, text = "+",width=3,command = add, font=("Comic Sans MS",24))
plus.grid(row=4,column=4,sticky="nsew")
minus = tkinter.Button(home, text = "—", font=("Comic Sans MS",24))
minus.grid(row=3,column=4,sticky="nsew")
equal = tkinter.Button(home, text = "=", command = answer,font=("Comic Sans MS",24))
equal.grid(row=5,column=4,sticky="nsew")
divide = tkinter.Button(home, text = "÷", font=("Comic Sans MS",24))
divide.grid(row=1,column=4,sticky="nsew")
multiply = tkinter.Button(home, text = "X",font=("Comic Sans MS",24))
multiply.grid(row=2,column=4,sticky="nsew")
AC = tkinter.Button(home, text = "AC",font=("Comic Sans MS",24))
AC.grid(row=1,column=0,sticky="nsew")
negative = tkinter.Button(home, text = "+/-",font=("Comic Sans MS",24))
negative.grid(row=1,column=1,sticky="nsew")
percent = tkinter.Button(home, text = "%",font=("Comic Sans MS",24))
percent.grid(row=1,column=2,sticky="nsew")


jony.mainloop()