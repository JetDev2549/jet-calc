#import numpy (later)
from tkinter import *
from tkinter import ttk

GUI = Tk()
GUI.title("Calculator in Python")
GUI.geometry('500x500')

result = StringVar()

def add():
	Paetong = int(first.get())+int(second.get())
	result.set(Paetong)

def subtract():
	Paetong = int(first.get())-int(second.get())
	result.set(Paetong)
def multiply():
	Paetong = int(first.get())*int(second.get())
	result.set(Paetong)

def divide():
	Paetong = int(first.get())//int(second.get())
	result.set(Paetong)

first = StringVar()
second = StringVar()




LName = ttk.Label(GUI,text='First Number')
LName.pack(pady=10)

EName = ttk.Entry(GUI,textvariable=first,font=('Comic Sans MS',15))
EName.pack(pady=10)

TName = ttk.Label(GUI,text='Second Number')
TName.pack(pady=10)

UName = ttk.Entry(GUI,textvariable=second,font=('Comic Sans MS',15))
UName.pack(pady=10)

calculate = ttk.Button(GUI,text='Add',command=add)
calculate.pack(ipadx=10,ipady=5)

calculate = ttk.Button(GUI,text='Subtract',command=subtract)
calculate.pack(ipadx=10,ipady=5)

calculate = ttk.Button(GUI,text='Multiply',command=multiply)
calculate.pack(ipadx=10,ipady=5)

calculate = ttk.Button(GUI,text='Divide',command=divide)
calculate.pack(ipadx=10,ipady=5)

Result = ttk.Label(GUI, textvariable=result,font=('Comic Sans MS',15))
Result.pack(pady=10)

GUI.mainloop()