from tkinter import *
import tkinter as tk

#import other modules
import student_tracking_assignment
import student_tracking_func

def load_gui(self):
    self.lbl_fname = tk.Label(self.master,text='First Name: ') #using prebuilt tkinter class Label and naming lbl_fname
    self.lbl_fname.grid(row=0,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_lname = tk.Label(self.master,text='Last Name: ')
    self.lbl_lname.grid(row=2,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_phone = tk.Label(self.master,text='Phone Number: ')
    self.lbl_phone.grid(row=4,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_email = tk.Label(self.master,text='Email: ')
    self.lbl_email.grid(row=6,column=0,padx=(27,0),pady=(10,0),sticky=N+W)

    self.lbl_current_course = tk.Label(self.master,text='Current Course: ')
    self.lbl_current_course.grid(row=8,column=0,padx=(27,0),pady=(10,0),sticky=N+W)
    #----------------------------------------------------------------------------

    self.txt_fname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=1,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_lname = tk.Entry(self.master,text='')
    self.txt_fname.grid(row=3,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_phone = tk.Entry(self.master,text='')
    self.txt_phone.grid(row=5,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_email = tk.Entry(self.master,text='')
    self.txt_email.grid(row=7,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    self.txt_current_course = tk.Entry(self.master,text='')
    self.txt_current_course.grid(row=9,column=0,rowspan=1,columnspan=2,padx=(30,40),pady=(0,0),sticky=N+E+W)

    #row 0/1 0/2 1/2
    #row 2/3 3/4 
    #row 4/5 5/6
    #row 6/7 7/8
    #row 8/9 9/10

    #define listbook with scrollbar and grid them
    self.scrollbar1 = Scrollbar(self.master,orient=VERTICAL)
    self.lstList1 = Listbox(self.master,exportselection=0,yscrollcommand=self.scrollbar1.set)
    self.lstList1.bind('<<ListboxSelect>>',lambda event: student_tracking_func.onSelect(self,event))
    self.scrollbar1.config(command=self.lstList1.yview)
    self.scrollbar1.grid(row=1,column=5,rowspan=8,columnspan=1,padx=(0,0),pady=(0,0),sticky=N+E+S)
    self.lstList1.grid(row=1,column=2,rowspan=8,columnspan=3,padx=(0,0),pady=(0,0),sticky=N+E+S+W)

    #buttons
    self.btn_delete = tk.Button(self.master,width=12,height=2,text='Delete',command=lambda: student_tracking_func.toDelete(self))
    self.btn_delete.grid(row=14,column=2,padx=(15,0),pady=(45,10),sticky=W) #may need to adjust
    self.btn_close = tk.Button(self.master,width=12,height=2,text='Close',command=lambda: student_tracking_func.ask_quit(self))
    self.btn_close.grid(row=14,column=3,columnspan=1,padx=(15,0),pady=(45,10),sticky=E)

    student_tracking_func.create_db(self)
    student_tracking_func.toRefresh(self)

if __name__ == "__main__":
    pass
