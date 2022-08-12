import tkinter as tk
from tkinter import *
import tkinter.filedialog
import os
import shutil
import datetime
from datetime import datetime, timedelta
import pytz
from pytz import timezone

class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self)
        #sets title of gui window
        self.master.title("File Transfer")

        #BUTTONS
        #creates button to select files from source directory
        self.sourceDir_btn = Button(text="Select Source", width=20, command=self.sourceDir)
        #positions source button in GUI using grid
        self.sourceDir_btn.grid(row=0, column=0, padx=(20, 10), pady=(30,0))
        #creates entry for source directory selection
        self.source_dir = Entry(width=75)
        #positions entry in gui using grid. padx and pady are same as button to line up
        self.source_dir.grid(row=0, column=1, columnspan=2, padx=(20, 10), pady=(30, 0))

        
    
        #creates button to select destination of files from destination directory
        self.destDir_btn = Button(text="Select Destination", width=20, command=self.destDir)
        #positions destination button in Gui using grid
        #on next row under source button
        self.destDir_btn.grid(row=1, column=0, padx=(20,10), pady=(15, 10))

        #creates entry for destination directory selection
        self.destination_dir = Entry(width=75)
        #positions entry in gui using grid. padx and pady are same as button
        self.destination_dir.grid(row=1, column=1, columnspan=2, padx=(20, 10), pady=(15, 10))

        #create button to transfer files
        self.transfer_btn = Button(text="Transfer Files", width=20, command=self.transferFiles)
        #postition transfer file button
        self.transfer_btn.grid(row=2, column=1, padx=(200, 0), pady=(0, 15))

        #create exit button
        self.exit_btn = Button(text="Exit", width=20, command=self.exit_program)
        #positions the exit button
        self.exit_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


        #button to practice functions on
        self.practice_btn = Button(text="Practice", width=20, command=self.checkNew)
        self.practice_btn.grid(row=2, column=2, padx=(10, 40), pady=(0, 15))


       

    #FUNCTIONS
    #function to select source directory
    def sourceDir(self):
        selectSourceDir = tkinter.filedialog.askdirectory()
        #the delete(0,END) will clear the content that is inserted in the entry widget
        #this allows the path to be inserted in the entry widget properly
        self.source_dir.delete(0, END)
        #the insert method will insert user selection to the source_dir Entry
        self.source_dir.insert(0, selectSourceDir)


    #creates function to select destination directory
    def destDir(self):
        selectDestDir= tkinter.filedialog.askdirectory()
        self.destination_dir.delete(0, END)
        self.destination_dir.insert(0, selectDestDir)

    def transferFiles(self):
        #get source directory
        source = self.source_dir.get()
        #gets destination directory
        destination = self.destination_dir.get()
        #gets a list of files in source directory
        source_files = os.listdir(source)
        curTime = datetime.now()
        curTime24 = curTime - timedelta(hours = 24)
        print(curTime24) #temp 
        for filename in source_files:
            filepath = os.path.join(source,filename)
            mTime = os.path.getmtime(filepath)
            conmTime = datetime.fromtimestamp(mTime)#.strftime('%H')
            print(conmTime) #temp
            if curTime24 < conmTime:
                shutil.move(source + '/' + filename, destination)
                print(filename + ' was successfully transferred.')

    #way to exit program
    def exit_program(self):
        #root is the main GUI window
        #destory method tells python to terminate root.mainloop and all widgets in GUI
        root.destroy()

        





                







            #Initial to do/pseudocode plan:
            #now store creation time as converted var similar to curTime24 os.path.getctime(path)
            #need a way to have seconds or time since file created as variable
            #then have if that time is <=24 hrs (curTime24) move files to destDir
            #now repeat above with modification time os.path.getmtime(path)
            
           


       


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
