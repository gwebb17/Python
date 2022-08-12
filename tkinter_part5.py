from tkinter import *
win = Tk()


#using StringVar to hold user entry as variable to use
v = StringVar()
e = Entry(win, textvariable = v)
e.pack()

#using get to display the variable string now
v.get()
#using set to set the text in the entry field
v.set("This is set by program")

#listbox makes a list to choose from created after opening window command (win = Tk())
lb = Listbox(win, height=3) #since listbox only set to 3 lines high, the 4th entry wont show below
lb.pack()
lb.insert(END, "First entry") #insert at the END with text first entry
lb.insert(END, "Second entry")
lb.insert(END, "third entry")
lb.insert(END, "fourth entry")

#make scrollbar to use with listbox and pack into the listbox
sb = Scrollbar(win, orient=VERTICAL)
sb.pack(side=LEFT, fill=Y)
#before it can work with listbox we need to configure them both to know each other
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)

#this would display whatever is highlighted/selected by cursor currently in listbox
lb.curselection()
