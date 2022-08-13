import tkinter as tk
from tkinter import *
import webbrowser #can create web dox and display in browser



class ParentWindow(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.master.title("Web Page Generator")

        
        #entry field may need to remove extra "Label" in names
        self.custom_entryLabel = tk.Label(self.master, text='Enter custom text or click the Default HTML page button')
        self.custom_entryLabel.grid(row=0,column=0)
        #entry
        self.custom_entry = tk.Entry(self.master, text='', width=100)  #trying to save text as var like textvariable=userText
        self.custom_entry.grid(row=1, padx=(10,10) , pady=(10,10))


        #default button
        self.btn = Button(self.master, text="Default HTML Page", width=30, height=2, command=self.defaultHTML)
        self.btn.grid(row=3, column=2, columnspan=2, padx=(10,10) , pady=(10,10))
        #submit custom button
        self.btn = Button(self.master, text="Submit Custom Text", width=30, height=2, command=self.customTextFunc)
        self.btn.grid(row=3, column=4, columnspan=2, padx=(10,10) , pady=(10,10))

        

    def defaultHTML(self):
        htmlText = "Default HTML Page"
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + htmlText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")

   
    def customTextFunc(self):
        userText = tk.StringVar(self.master, tk.Entry)   #define window that is assoc with Entry/parent window
        convUserText = userText.get()
        htmlText = convUserText
        htmlFile = open("index.html", "w")
        htmlContent = "<html>\n<body>\n<h1>" + convUserText + "</h1>\n</body>\n</html>"
        htmlFile.write(htmlContent)
        htmlFile.close()
        webbrowser.open_new_tab("index.html")
    


if __name__ == "__main__":
    root = tk.Tk()
    App = ParentWindow(root)
    root.mainloop()
    
