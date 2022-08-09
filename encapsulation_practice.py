#create class
class Coffee:
    def __init__(self):
        self.__pounds = 7
        self._roast = "dark"

    #create privatevariable
    def getPounds(self):
        #print(self.__pounds)
        return self.__pounds
    

    #create protectedvariable
    def setPounds(self, pounds):
        self.__pounds = pounds 

#create object of the class Coffee()
coffeeObj = Coffee()

#because __pounds is private we need to call the function printPrvVar to access
#the pounds variable
weight = coffeeObj.getPounds()
print(weight)

#because the _roast var is protected not private we can directly print it
#without calling function
print(coffeeObj._roast)

#can pass in new argument for __pounds by having it as another parameter in
#the above function printProVar
#this does not refer to the built in SET method previously used
coffeeObj.setPounds(10)
#now __pounds = 10 so the function printPrvVar now displays 10
#below combines both lines 22-23 into single statement
print(coffeeObj.getPounds())


#changing __pounds value again and displaying again new value
coffeeObj.setPounds(4)
print(coffeeObj.getPounds())

   
