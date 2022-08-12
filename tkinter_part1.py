from tkinter import *

#creates window
win = Tk()

#creating buttons
b1 = Button(win, text="One")
b2 = Button(win, text="Two")



#using pack instead of grid, defaults to top but can say TOP, LEFT, RIGHT, BOTTOM
#pack is used when placing things in vertical column or horizontal row
b1.pack() 
b2.pack()

#using LEFT, first puts b1 at far left then puts b2 next to it to the right of it
b1.pack(side=LEFT)
b2.pack(side=LEFT)


#using padding to add space between buttons.
#padx adds pixels to left and right
#pady adds to top and bottom
b1.pack(side = LEFT, padx = 10)
b2.pack(side = LEFT, padx = 10)


#create more practice buttons
#can combine above statements into simpler one below
mrClicky = Button(win, text="Mr. Clicky")
mrsClicky = Button(win, text="Mrs. Clicky")
mrClicky.pack(side=RIGHT, pady=30)
mrsClicky.pack(side=RIGHT, pady=30)
