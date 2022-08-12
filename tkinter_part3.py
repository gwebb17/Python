from tkinter import *

#create window
win = Tk()
b1 = Button(win, text="One")
b2 = Button(win, text="Two")
b1.grid(row=0, column=0)
b2.grid(row=1, column=1)


#use label to place text in window
#expands column width to accomodate the string in row 1
l = Label(win, text="This is a label")
l.grid(row=1, column=0)

#frame is widget that contains other widgets. Groups of other widgets can be
#combined in a single frame
win = Tk()
f = Frame(win)
b1 = Button(f, text="One")
b2 = Button(f, text="Two")
b3 = Button(f, text="Three")
b1.pack(side=LEFT)
b2.pack(side=LEFT)
b3.pack(side=LEFT)
l = Label(win, text="This label is over all buttons")
l.pack()
f.pack()

#if grid cell is bigger than your widget because a larger widget is in
#the same row or column, use sticky N,E,S,W,NE etc to position

#changes button text from One to Uno using configure
b1.configure(text="Uno")

#using function that displays a string when button b1 is clicked
def but1():
    print("Button one was pushed")

b1.configure(command=but1)
