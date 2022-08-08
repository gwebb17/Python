from tkinter import *
import tkinter as tk

"""the reason the fname column doesn't have field is because its used in place of the "fullname" column in prev example"""

#import other modules if needed
import student_tracking_gui
import student_tracking_func

#parent class frame
class ParentWindow(Frame):
    def __init__ (self,master,*args,**kwargs):
        Frame.__init__(self,master,*args,**kwargs)

        self.master = master
        self.master.minsize(600,400)
        self.master.maxsize(600,400)

        self.master.title("Student Tracking")
        self.master.configure(bg="purple")

        #catch if X close is clicked
        self.master.protocol("WM_DELETE_WINDOW", lambda: student_tracking_func.ask_quit(self))
        """create function in separate file student_tracking_func called ask_quit() that has message"""
        arg = self.master


        #load separate GUI to be created student_tracking_gui
        student_tracking_gui.load_gui(self)
        #need to call function intial run somewhere



if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
