from abc import ABC, abstractmethod


#parent class
class Rocks:
    def RockType(self):
        kind = input("What kind of rock do you have? ")
        print("This is a {} rock.".format(kind))

    @abstractmethod
    def RockWeight(self):
        pass

   
class Saphires(Rocks):
    def RockWeight(self):
        weight = input("How heavy is your rock? ")
        x = int(weight)
        
        if x > 15 and x < 30:
            print("Rocks are heavy objects")
        elif x > 30 and x < 70:
            print("That's a heavy rock")
        elif x > 70:
            print("That's a very heavy rock")
        else:
            print("Find a bigger rock")
    

rockOne = Rocks()
rockOne.RockType()
rockTwo = Saphires()
rockTwo.RockWeight()
