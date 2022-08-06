def displayGuitar():
        x = input("What brand of guitar do you have?")
        print("We don't carry {} guitars here".format(x))


class Guitar:
  Make = "Fender"
  Model = "Telecaster"
  Frets = "24"
      

class Acoustic(Guitar):
    Steel_or_Nylon: "Steel"
    Wood: "Rosewood"

class Electric(Guitar):
    Seven_String: False
    Volume_Knobs: 2

#prints Elements of guitar class
print(vars(Guitar))
    
        

#create new instance of object in class Guitar        
new_Guitar = Guitar()
#call function to print something to display
displayGuitar()


      

