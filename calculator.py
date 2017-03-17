from tkinter import *
from tkinter import messagebox

about = "A simple calculator in Python 3.5.2 using the Tkinter module for GUI programming. \nAuthor: Leo Hajder (leohajder.github.io)"

#initialization
app = Tk()
app.title("Calculator")
app.resizable(width=False, height=False) #fixed 1st bug

#menu
menubar = Menu(app)
filemenu = Menu(menubar, tearoff = 0)
filemenu.add_command(label = "About", command = lambda: messagebox.showinfo("About", about))
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = app.destroy)
menubar.add_cascade(label = "File", menu = filemenu)
app.config(menu=menubar)

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
        if(storeBuffer != ""): #fixed bug: prevent clear if 2 operators clicked in a row
            storeMemory = eval(str(float(storeMemory)) + str(storeOperator) + str(float(storeBuffer)))
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

#key binding
def key(event):
    if(event.keysym == "Return"):
        click("=")
    elif(event.keysym == "plus"):
        click("+")
    elif(event.keysym == "minus"):
        click("-")
    elif(event.keysym == "asterisk"):
        click("*")
    elif(event.keysym == "slash"):
        click("/")
    elif(event.keysym == "comma"):
        click(".")
    elif(event.keysym.isdigit()):
        click(event.keysym)
    elif(event.keysym in ["c", "Escape"]):
        clear()

app.bind("<Key>", key)

#gui elements
display = Entry(app, state = DISABLED, justify = RIGHT, bd = 2, disabledbackground = "pale green", textvariable = displayText).grid(row = 0, column = 0, columnspan = 4, ipadx = 5, ipady = 5, padx =5, pady = 5)
btnClear = Button(app, text = "C", command = lambda: clear(), bg = "indian red", fg = "white").grid(row = 1, column = 0, ipadx = 5)
btnDivide = Button(app, text = "/", command = lambda: click("/"), bg = "light blue", fg = "white").grid(row = 1, column = 1, ipadx = 5)
btnMultiply = Button(app, text = "*", command = lambda: click("*"), bg = "light blue", fg = "white").grid(row = 1, column = 2, ipadx = 5)
btnSubtract = Button(app, text = "-", command = lambda: click("-"), bg = "light blue", fg = "white").grid(row = 1, column = 3, ipadx = 5)
btn7 = Button(app, text = "7", command = lambda: click("7")).grid(row = 2, column = 0, ipadx = 5, pady = 2)
btn8 = Button(app, text = "8", command = lambda: click("8")).grid(row = 2, column = 1, ipadx = 5, pady = 2)
btn9 = Button(app, text = "9", command = lambda: click("9")).grid(row = 2, column = 2, ipadx = 5, pady = 2)
btnAdd = Button(app, text = "+", command = lambda: click("+"), bg = "light blue", fg = "white", height = 1, width = 1).grid(row = 2, column = 3, rowspan = 2, ipadx = 5, ipady = 14)
btn4 = Button(app, text = "4", command = lambda: click("4")).grid(row = 3, column = 0, ipadx = 5, pady = 2)
btn5 = Button(app, text = "5", command = lambda: click("5")).grid(row = 3, column = 1, ipadx = 5, pady = 2)
btn6 = Button(app, text = "6", command = lambda: click("6")).grid(row = 3, column = 2, ipadx = 5, pady = 2)
btn1 = Button(app, text = "1", command = lambda: click("1")).grid(row = 4, column = 0, ipadx = 5, pady = 2)
btn2 = Button(app, text = "2", command = lambda: click("2")).grid(row = 4, column = 1, ipadx = 5, pady = 2)
btn3 = Button(app, text = "3", command = lambda: click("3")).grid(row = 4, column = 2, ipadx = 5, pady = 2)
btnEquals = Button(app, text = "=", command = lambda: click("="), bg = "light blue", fg = "white", height = 1, width = 1).grid(row = 4, column = 3, rowspan = 2, ipadx = 5, ipady = 14)
btn0 = Button(app, text = "0", command = lambda: click("0")).grid(row = 5, column = 0, columnspan = 2, ipadx = 20, pady = 2)
btnDecimal = Button(app, text = ",", command = lambda: click(".")).grid(row = 5, column = 2, ipadx = 7, pady = 2)

clear() #setup on load

app.focus_force()

app.mainloop()
