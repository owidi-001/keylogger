from tkinter import *
from tkinter import messagebox

# Top level window
window = Tk()
window.title("TextBox Input")
window.geometry('400x200')
# Function for getting Input
# from textbox and printing it 
# at label widget
  
def printInput():
    inp = inputtxt.get(1.0, "end-1c")
    lbl.config(text = "Provided Input: "+inp)
  
# TextBox Creation
inputtxt = Text(window,
                   height = 5,
                   width = 20)
  
inputtxt.pack()
  
# Button Creation
printButton = Button(window,
                        text = "Print", 
                        command = printInput)
printButton.pack()
  
# Label Creation
lbl = Label(window, text = "")
lbl.pack()
window.mainloop()