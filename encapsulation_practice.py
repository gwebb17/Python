#create class
class Coffee:
    def __init__(self):
        self.__pounds = 7
        self._roast = "dark"

    #create privatevariable
    def printPrvVar(self):
        print(self.__pounds)

    #create protectedvariable
    def printProVar(self, pounds):
        self.__pounds = pounds 

#create object of the class Coffee()
coffeeObj = Coffee()

#because __pounds is private we need to call the function printPrvVar to access
#the pounds variable 
coffeeObj.printPrvVar()

#because the _roast var is protected not private we can directly print it
#without calling function
print(coffeeObj._roast)

#can pass in new argument for __pounds by having it as another parameter in
#the above function printProVar
coffeeObj.printProVar(10)
#now __pounds = 10 so the function printPrvVar now displays 10
coffeeObj.printPrvVar()

#changing __pounds value again and displaying again new value
coffeeObj.printProVar(4)
coffeeObj.printPrvVar()

   
