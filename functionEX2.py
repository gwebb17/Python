def functionSeven():
    go = True
    while go:
        answer = input("The Colossus of ___")
        if answer =="":
            print("blank answer you are wrong")
        elif answer == "Roads":
            print("Check your spelling")
        elif answer == "Rhoades":
            print("congratulations you are smart") 
        else:
            go = False

functionSeven()
