class Piano: #parent class
    Make = "Unknown"
    Model = "Unknown"
    Keys = 88
    Pedals = 3

    #method for parent class
    def getInfo(self):
        display1 = "Piano make: {}\nModel: {}\nKeys: {}\nPedals: {}".format(self.Make, self.Model, self.Keys, self.Pedals)
        return display1

#child class 1
class Kawai(Piano):
    Make = "Kawai"
    Model = "ES-8"
    Digital = "digital"
    Midi = "MIDI"
    #child class 1 method demonstrating polymorphism
    def getInfoK(self):
        displayK = input("Are you interested in learning more about Kawai pianos? (Y/N)")
        if (displayK == "Y"):
            print("The {} {} is {} and has {} capabilities".format(self.Make,self.Model,self.Digital,self.Midi))
        else:
            print("Ok bye")

#child class 2
class Roland(Piano):
    Make = "Roland"
    Model = "R2-A"
    Weight = "47 lbs"
    Serial = 344888902
    #child class 2 method
    def getInfoR(self):
        displayR = input("How about Roland pianos? (Y/N)")
        if (displayR == "Y"):
            print("The {} {} is only {}, here's the reference serial #: {}".format(self.Make,self.Model,self.Weight,self.Serial))
        else:
            print("Ok bye again")



if __name__ == "__main__":
    kawai = Kawai()  #create object/instance of Kawai class 
    print(kawai.getInfo())
    kawai.getInfoK()
    roland = Roland() #create object/instance of Roland class
    print(roland.getInfo())
    roland.getInfoR()
    
