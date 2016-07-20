'''
A simple calculator application made for fun and practice
with Python 3.5.2 using the Tkinter module for GUI programming.
Author: Leo Hajder (github.com/lhajder)
'''

#GUI module
from tkinter import *

#initialization
calculator = Tk()

#menu
menubar = Menu(calculator)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "About", command = lambda: messagebox.showwarning("About", "A simple calculator application made for fun and practice with Python 3.5.2 using the Tkinter module for GUI programming. \nAuthor: Leo Hajder (github.com/lhajder)"))
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = calculator.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
calculator.config(menu=menubar)

#variables and functions
storeBuffer = ""
storeMemory = 0
storeOperator = "+"
displayText = StringVar()

def click(key):
    global storeBuffer, storeMemory, storeOperator
    if(key.isdigit() or key == "."):
        storeBuffer +=  key
        displayText.set(storeBuffer)
    elif(key == "="):
        result()
        storeOperator = "+"
        storeBuffer = ""
    else:
        result()
        storeOperator = key
        storeBuffer = ""
        return

def result():
    global storeBuffer, storeMemory, storeOperator, displayText
    try:
        storeMemory = eval(str(float(storeMemory)) + str(storeOperator) + str(float((storeBuffer) or 0))) #or 0 --> if storeBuffer is empty string, treat it as 0 when calculating
        if(storeMemory == int(storeMemory)):
            storeMemory = int(storeMemory) #just to remove the decimal point from the screen if it's not needed
        displayText.set((str(storeMemory)))
        return
    except:
        displayText.set("Math error") #dividing by 0 etc.
        return

def clear():
    global storeBuffer, storeMemory, storeOperator
    storeBuffer = ""
    storeMemory = 0
    storeOperator = "+"
    result()
    
#gui elements
display = Entry(calculator, state = DISABLED, justify = RIGHT, bd = 2, disabledbackground = "pale green", textvariable = displayText).grid(row = 0, column = 0, columnspan = 4, ipadx = 5, ipady = 5, padx =5, pady = 5)
btnClear = Button(calculator, text = "C", command = lambda: clear(), bg = "indian red", fg = "white").grid(row = 1, column = 0, ipadx = 5)
btnDivide = Button(calculator, text = "/", command = lambda: click("/"), bg = "light blue", fg = "white").grid(row = 1, column = 1, ipadx = 5)
btnMultiply = Button(calculator, text = "*", command = lambda: click("*"), bg = "light blue", fg = "white").grid(row = 1, column = 2, ipadx = 5)
btnSubtract = Button(calculator, text = "-", command = lambda: click("-"), bg = "light blue", fg = "white").grid(row = 1, column = 3, ipadx = 5)
btn7 = Button(calculator, text = "7", command = lambda: click("7")).grid(row = 2, column = 0, ipadx = 5, pady = 2)
btn8 = Button(calculator, text = "8", command = lambda: click("8")).grid(row = 2, column = 1, ipadx = 5, pady = 2)
btn9 = Button(calculator, text = "9", command = lambda: click("9")).grid(row = 2, column = 2, ipadx = 5, pady = 2)
btnAdd = Button(calculator, text = "+", command = lambda: click("+"), bg = "light blue", fg = "white", height = 1, width = 1).grid(row = 2, column = 3, rowspan = 2, ipadx = 5, ipady = 14)
btn4 = Button(calculator, text = "4", command = lambda: click("4")).grid(row = 3, column = 0, ipadx = 5, pady = 2)
btn5 = Button(calculator, text = "5", command = lambda: click("5")).grid(row = 3, column = 1, ipadx = 5, pady = 2)
btn6 = Button(calculator, text = "6", command = lambda: click("6")).grid(row = 3, column = 2, ipadx = 5, pady = 2)
btn1 = Button(calculator, text = "1", command = lambda: click("1")).grid(row = 4, column = 0, ipadx = 5, pady = 2)
btn2 = Button(calculator, text = "2", command = lambda: click("2")).grid(row = 4, column = 1, ipadx = 5, pady = 2)
btn3 = Button(calculator, text = "3", command = lambda: click("3")).grid(row = 4, column = 2, ipadx = 5, pady = 2)
btnEquals = Button(calculator, text = " = ", command = lambda: click("="), bg = "light blue", fg = "white", height = 1, width = 1).grid(row = 4, column = 3, rowspan = 2, ipadx = 5, ipady = 14)
btn0 = Button(calculator, text = "0", command = lambda: click("0")).grid(row = 5, column = 0, columnspan = 2, ipadx = 20, pady = 2)
btnDecimal = Button(calculator, text = ",", command = lambda: click(".")).grid(row = 5, column = 2, ipadx = 7, pady = 2)

clear() #setup on load

calculator.mainloop()
