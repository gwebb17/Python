


#parent class template for future objects to be built with
class Organism: #naming convention for class has Capital 1st letter usually
    name = "Unknown"
    species = "Unknown"
    legs = None #special data type
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    #define method for parent class that can be used by other classes
    def information(self): #needs to have self keyword to have access to attributes
        msg = "\nName: {}\nSpecies: {}\nLegs: {}\nArms: {}\nDNA: {}\nOrigin: {}:\nCarbon_based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.origin,self.carbon_based)
        #need to use self.attributename above in .format to access data
        return msg

#child class instance
class Human(Organism): #in order to use parent class properties need to reference it in () here
    name = "MacGyver"
    species = "Homosapien"
    legs = 2
    arms = 2
    origin = "Earth"
    #other property of carbon_based will be inherited since not listed here

    def ingenuity(self):
        msg = "\nCreates a deadly weapon using only a paperclip, chewing gum and duct tape"
        return msg

#add another child class
class Dog(Organism):
    name = "Spot"
    species = "canine"
    legs = 4
    arms = 0
    dna = "Sequence B" #since different than parent we list this here
    origin = "Earth"

    def bite(self):
        msg = "\nBite a person"
        return msg

#add another child class
class Bacterium(Organism):
    name = "X"
    species = "Bacteria"
    legs = 0
    arms = 0
    dna = "Sequence c"
    origin = "Mars"

    def replication(self):
        msg = "\nDivides cells and splits"
        return msg









if __name__ == "__main__":
    human = Human() #instantiating Human class and giving the name human
    print(human.information()) #human is now named so can be used to access method in parent class
    print(human.ingenuity()) #also call method defined in same class

    dog = Dog() #instantiated dog object and named dog
    print(dog.information())
    print(dog.bite())

    bacteria = Bacterium()
    print(bacteria.information())
    print(bacteria.replication())
    
