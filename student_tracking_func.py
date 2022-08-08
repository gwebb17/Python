import os
from tkinter import *
import tkinter as tk
import sqlite3
from tkinter import messagebox

#import other modules
import student_tracking_assignment
import student_tracking_gui

def keep_things_centered(self, w, h): #self=frame(master) parameters=w,h)
    screen_width = self.master.winfo_screenwidth()
    screen_height = self.master.winfo_screenheight()
    #using x/y center app on user screen
    x = int((screen_width/2) - (w/2))
    y = int((screen_height/2) - (h/2))
    centerCoord = self.master.geometry(' {}x{}+{}+{}'.format(w, h, x, y))
    return centerCoord

#function to display "are you sure you want to quit" message/and close app
def ask_quit(self):
    if messagebox.askokcancel("Are you sure you want to quit?"):
    #closes app
        self.master.destroy()
        os._exit(0) #prevents memory leaks

#create database
def create_db(self):
    conn = sqlite3.connect('student_tracking_assignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute("CREATE TABLE if not exists student_assignment_table( \
            ID INTEGER PRIMARY KEY AUTOINCREMENT, \
            col_fname TEXT, \
            col_lname TEXT, \
            col_phone TEXT, \
            col_email TEXT, \
            col_currentcourse TEXT \
            );")
        conn.commit()
    conn.close()
    initial_run(self)

#first run 
def initial_run(self):
    conn = sqlite3.connect('student_tracking_assignment.db')
    with conn:
        cur = conn.cursor()
        cur,count = count_records(cur)
        if count < 1:
            cur.execute("""INSERT INTO student_assignment_table (col_fname, col_lname, col_phone, col_email, col_currentcourse) VALUES (?,?,?,?,?)""",('Blankety', 'Blank', '308-233-2929', 'blank_slate@fake.gov', 'Studies in Not Forgetting Semicolons'))
            conn.commit()
    conn.close()

def count_records(cur):
    count = ""
    cur.execute("""SELECT COUNT(*) FROM student_assignment_table""") #counting up all rows
    count = cur.fetchone()[0] #corresponds to first index from above function(initial_run) tuple
    return cur,count

def onSelect(self,event):
    varList = event.widget
    select = varList.curselection()[0]
    value = varList.get(select)
    conn = sqlite3.connect('student_tracking_assignment.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT col_fname,col_lname,col_phone,col_email,col_currentcourse FROM student_assignment_table WHERE col_fname = (?)""", [value])
        varBody = cursor.fetchall()
        for data in varBody:
            self.txt_fname.delete(0,END)
            self.txt_fname.insert(0,data[0])
            self.txt_lname.delete(0,END)
            self.txt_lname.insert(0,data[1])
            self.txt_phone.delete(0,END)
            self.txt_phone.insert(0,data[2])
            self.txt_email.delete(0,END)
            self.txt_email.insert(0,data[3])
            self.txt_current_course.delete(0,END)
            self.txt_current_course.insert(0,data[4])
            


#function to delete row/record
def toDelete(self):
    var_select = self.lstList1.get(self.lstList1.curselection()) #selected value from listbox
    conn = sqlite3.connect('student_tracking_assignment.db')
    with conn:
        cur = conn.cursor()
        cur.execute("""SELECT COUNT (*) FROM student_assignment_table""")
        count = cur.fetchone()[0]
        if count > 0:
            confirm = messagebox.askokcancel("Confirm delete? This action cannot be undone")
            if confirm:
                conn = sqlite3.connect('student_tracking_assignment.db')
                with conn:
                    cursor = conn.cursor()
                    cursor.execute("""DELETE FROM student_assignment_table WHERE col_fname = '{}'""".format(var_select))
                toDeleted(self) #calls function to clear textboxes/selected index of listbox
                conn.commit()
        else:
            confirm = messagebox.showerror("Last record in list cannot be deleted")
    conn.close()

def toDeleted(self):
    #clears text in these textboxes
    self.txt_fname.delete(0,END) #0 END denotes selecting entire row from 0 to the end
    self.txt_lname.delete(0,END)
    self.txt_phone.delete(0,END)
    self.txt_email.delete(0,END)

    #toRefresh(self) update listbox of changes
    try:
        index = self.lstList1.curselection()[0]
        self.lstList1.delete(index)
    except IndexError:
        pass

def toRefresh(self):
    self.lstList1.delete(0,END) #delete everything in listbox so it can be refreshed with current data
    conn = sqlite3.connect('student_tracking_assignment.db')
    with conn:
        cursor = conn.cursor()
        cursor.execute("""SELECT COUNT (*) FROM student_assignment_table""") #select everything from the table
        count = cursor.fetchone()[0]
        i = 0
        while i < count:
            cursor.execute("""SELECT col_fname FROM student_assignment_table""")
            varList = cursor.fetchall()[i]
            for item in varList:
                self.lstList1.insert(0,str(item))
                i = i + 1
    conn.close()


#i dont think this is needed but not sure what is causing issue
def onUpdate(self):
    try:
        var_select = self.lstList1.curselection()[0] #index of list selection
        var_value = self.lstList1.get(var_select) #list selection text value
    except:
        messagebox.showinfo("Missing selection", "No name was selected from the list box \nCancelling the Update request.")
        return
    #user will only be allowed to update changes for phone and emails
    #for name changes the user needs to delete entire record and start over
    var_phone = self.txt_phone.get().strip() #normalize data to maintain database integrity
    var_email = self.txt_email.get().strip()
    if (len(var_phone) > 0) and (len(var_email) > 0): #ensure data is present
        conn = sqlite3.connect('db_phonebook.db')
        with conn:
            cur = conn.cursor()
            #count records to see if changes are already in
            #the database, meaning there are no changes to update
            cur.execute("""SELECT COUNT(col_phone) FROM tbl_phonebook WHERE col_phone = '{}'""".format(var_phone))
            count = cur.fetchone()[0]
            print(count2)
            if count == 0 or count2 == 0: #if proposed changes aren't in database, then proceed
                response = messagebox.askokcancel("Update Request", "The following changes ({}) and ({}) will be implemented for ({}). \nProceed with the update request?".format(var_phone,var_email,var_value))
                print(response)
                if response:
                    #conn = sqlite3.connect('db_phonebook.db') <<Uncomment???
                    with conn:
                        cursor = conn.cursor()
                        cursor.execute("""UPDATE tbl_phonebook SET col_phone = '{0}',col_email = '{1}' WHERE col_fullname = '{2}'""".format(var_phone,var_email,var_value))
                        onClear(self)
                        conn.commit()
                else:
                    messagebox.showinfo("Cancel Request","No changes have been made to ({}).".format(var_value))
            else:
                messsagebox.showinfo("No changes detected", "Both ({}) and ({}) \nalready exist in the database for this name. \n\nYour update request has been cancelled.".format(var_phone,var_email))
            onClear(self)
        conn.close()
    else:
        messagebox.showerror("Missing information", "Please select a name from the list. \nThen edit phone or email information.")
    onClear(self)    

if __name__ == "__main__":
    pass
        
        
            
