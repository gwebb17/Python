from tkinter import * #* denotes to import everything
import tkinter as tk

#import other modules so we can access them
import phonebook_gui
import phonebook_func

#Frame is the Tkinter frame class that our own class will inherit from
class ParentWindow(Frame):  #frame means we're taking inheriting structure of built in Frame from Tkinter
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        #define our master frame configuration
        #without saying "self" we can't access previously defined things/stuff
        self.master = master #self refers to class ParentWindow 
        self.master.minsize(500,300) #Height, Width)
        self.master.maxsize(500,300)
        #the CenterWindow method will center our app on the users screen
        phonebook_func.center_window(self,500,300) #this line accesses the imported modules from above import statement
        self.master.title("The Tkinter Phonebook Demo")
        self.master.configure(bg="#F0F0F0")
        #this protocol method is a tkinter built in method to catch if
        #the user clicks the upper corner "X" on Windows OS.
        self.master.protocol("WM_DELETE_WINDOW", lambda: phonebook_func.ask_quit(self)) #this function: ask_quit will be from separate module
        arg = self.master

        #load in the GUI widgets from a separate module
        #keeping your code comparmentalized and cluster free
        phonebook_gui.load_gui(self)

        #instantiate the tkinter menu dropdown object
        #this is the menu that will appear at the top of our window
        menubar = Menu(self.master)
        filemenu = Menu(menubar, tearoff=0)
        filemenu.add_separator()
        filemenu.add_command(label="Exit", underline=1, accelerator="Ctrl+Q",command=lambda: phonebook_func.ask_quit(self))
        menubar.add_cascade(label="File", underline=0, menu=filemenu)
        helpmenu = Menu(menubar, tearoff=0) #defines dropdown column and tearoff=0 means don't separate from menubar
        helpmenu.add_separator()
        helpmenu.add_command(label="How to use this program")
        helpmenu.add_separator()
        helpmenu.add_command(label="About This Phonebook Demo")
        menubar.add_cascade(label="Help", menu=helpmenu)

        #apply config method of widget to display menu
        self.master.config(menu=menubar, borderwidth='1')


if __name__ == "__main__": #When python see's this skip everything above and only run below i think
    root = tk.Tk() #syntax to create window
    App = ParentWindow(root) #something necessary and uses class name
    root.mainloop() #syntax to end loop when prompted
