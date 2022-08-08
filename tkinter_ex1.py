import tkinter
from tkinter import *

class ParentWindow(Frame):
    def __init__ (self, master):#can now reference class as self and frame as master
        Frame.__init__ (self)

        self.master = master
        self.master.resizable(width=False, height=False) #cant resize window
        self.master.geometry('{}x{}'.format(700, 400)) #will make 700px wide by 400 px wide
        self.master.title('Learning Instructions')
        self.master.config(bg='lightgray')#change background color

        self.varFname = StringVar() #creating a string var called varFname
        self.varLname = StringVar()

        self.lblFname = Label(self.master, text='First Name: ', font=("Helvetica", 16), fg='black', bg='lightgray') #creating label for below txt boxes
        self.lblFname.grid(row=0, column=0, padx=(30, 0), pady=(30)) #0's mean upper left hand side. like cell 0 in row 0 . like an indice counting way
        #creates label for text box varname is lblFname and .self to reference class. then giving label properties
        self.lblLname = Label(self.master, text='Last Name: ', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblLname.grid(row=1, column=0, padx=(30, 0), pady=(30)) #same for last name

        self.lblDisplay = Label(self.master, text='', font=("Helvetica", 16), fg='black', bg='lightgray')
        self.lblDisplay.grid(row=3, column=1, padx=(30, 0), pady=(30))

        self.txtFname = Entry(self.master, text =self.varFname, font=("Helvetica", 16), fg='black', bg='lightblue')#creates txt box
        self.txtFname.grid(row=0, column=1) #creates txt box for Fname var

        self.txtLname = Entry(self.master, text =self.varLname, font=("Helvetica", 16), fg='black', bg='lightblue')#creates txt box
        self.txtLname.grid(row=1, column=1) #creates txt box for Lname var using grid. grid needs paremters of row and column
        #fg means foreground bg means background
        #USING GRID ABOVE means you have to use grid for all labels here too, can't mix PACK and GRID in same area.

        # PADX(horizontal) and PADY(Vertical) to control padding on side of text boxes. first value
        #first value in PADY is from the top second is from bottom. first in PADX is from right second is from the left

        #button submit
        self.btnSubmit = Button(self.master, text="Submit", width =10, height=2, command=self.submit) #names button btnSubmit and then says its a Button(where to place, and what it says
        self.btnSubmit.grid(row=2, column=1, padx=(0,0), pady=(30,0), sticky=NE)#says sticky position at upper right

        #button cancel
        self.btnCancel = Button(self.master, text="Submit", width =10, height=2, command=self.cancel)
        self.btnSubmit.grid(row=2, column=1, padx=(0,90), pady=(30,0), sticky=NE)


    #function for button submit needs to be same level as above method def
    def submit(self):
        fn = self.varFname.get() #use get to retrieve value from this element
        ln = self.varLname.get()
        self.lblDisplay.config(text='Hello {} {}'.format(fn, ln)) #.config dynamically changes something

    def cancel(self):
        self.master.destroy() #command to close the window when cancel is clicked
        
        



if __name__ == "__main__":
    root = Tk()
    App = ParentWindow(root)
    root.mainloop()  #important otherwise window will open and disappear. keeps loop alive until closed
