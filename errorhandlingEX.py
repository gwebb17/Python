def getInfo():
    var1 = input("\nPlease provide the first numeric value: ")
    var2 = input("\nPlease provide the second numeric value: ")
    return var1, var2



def compute():
    go = True
    while go: #saying while go is true, which is always
        var1, var2 = getInfo() #var1 and var2 equal what is returned from input 
        try: #if inputs are correct print as expected below
            var3 = int(var1) + int(var2) #convert var1 and var2 to ints
            go = False #if inputs correct end loop by making GO= false now
        except ValueError as e: #when this error happens print below
            print("{}: You did not provide a numeric value!".format(e))
        except: #for anything else print below
            print("\n\nOops the program will close now")
    print("{} + {} = {}".format(var1, var2, var3))
  

"""the as e above means that the ValueError is stored as a variable (e) and then
below it we use {} wildcard and .format(e) to say put the e here and format it
as a string"""


if __name__ == "__main__":
    compute()
