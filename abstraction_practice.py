from abc import ABC, abstractmethod #syntax anytime you use abstract methods


#parent class
class Rocks:
    def RockType(self):
        kind = input("What kind of rock do you have? ")
        print("This is a {} rock.".format(kind))

    #basically we are saying this method is not defined yet but will be
    #sort of like a placeholder
    @abstractmethod
    def RockWeight(self):
        pass

#child class    
class Saphires(Rocks):
    def RockWeight(self):
        weight = input("How heavy is your rock? ")
        x = int(weight) #convert input into integer/usable format
        
        if x > 15 and x < 30:
            print("Rocks are heavy objects")
        elif x > 30 and x < 70:
            print("That's a heavy rock")
        elif x > 70:
            print("That's a very heavy rock")
        else:
            print("Find a bigger rock")
            #above comparison statement doesn't work using "return"
    
#create instance of Rock object
rockOne = Rocks()
#now we can use its functions
rockOne.RockType()

#create instance of child class object
rockTwo = Saphires()
#use previously undefined method that is now defined within this class
rockTwo.RockWeight()
