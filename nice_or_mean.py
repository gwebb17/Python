from PIL import Image



                     
def start():
    f_name = "Sarah"
    l_name = "Connor"
    age = 28
    gender = "Female"
    get_info(f_name, l_name, age, gender)

def get_info(f_name, l_name, age, gender):
        print("My name is {} {}. I am a {} year old {}.".format(f_name, l_name, age, gender))
    

#the == 0 part means these are the default values for the parameters in case user doesn't input anything
#the 0 /default value also helps in the nice_mean function while saying (nice +1) gives it the base value of 0
def start(nice=0, mean=0, name=""):
    #get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name) #assigning multiple variables at once

def describe_game(name):
    """
    check if this is a new game or not.
    If it is new, get the user's name
    If it is not a new game, thank the player
    for playing again and continue with game
    """
    #meaning if we don't have user's name
    #than they are a new player and we need to get their name
    if name != "":
        print("\nThank you for playing again. {}".format(name))
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\nWhat is your name \n>>> ").capitalize()
                if name != "":
                    print("\nWelcome, {}!".format(name))
                    print("\nIn this game, you will be greeted \n by several different people.\nYou can choose to be nice or mean")
                    print("but at the end of the game your fate \nwill be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\nA stranger approaches you for a \nconversation. Will you be nice \nor mean? (N/M) \n>>>: ").lower()
        if pick == "n":
            print("\nThe stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print("\nThe stranger glares at you \nmenacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) #pass the 3 variables to the score


def show_score(nice,mean,name):
    print("\n{}, your current total: \n({}, Nice) and  ({}, Mean)".format(name,nice,mean))


def score(nice,mean,name):
    #score function is being passed the values stored within the 3 variables
    if nice > 2:  #if condition is valid call win function passing it the variables so it can use them
        win(nice,mean,name)
    if mean > 2:  # if condition valid, call lose function
        lose(nice,mean,name)
    else:   #otherwise call nice_mean function again to get more values/ask more questions
        nice_mean(nice,mean,name)

def win (nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nNice job {}, you win! \nEveryone loves you and you've \nmade lots of friends along the way!".format(name))
    img = Image.open("fireworks.jpg"); #when win called show win photo
    img.show();
    #call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #substitute the {} wildcards with our variable values
    print("\nAhh too bad, game over! \n{}, you live in a dirty beat-up \nvan by the river, wretched and alone!".format(name))
    img = Image.open("van.jpg");
    img.show();#when lose called show lose photo
    again(nice,mean,name)



    
def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\nDo you want to play again? (y/n)\n>>> ").lower()
        if choice == "y":
            reset(nice,mean,name)  #reset will reset the game to play again
        if choice == "n":
            print("\nOh so sad, sorry to see you go!")
            stop = False
            quit() #built in function will prompt user to close Python in IDLE or close program in actual application
        else:
            print("\nEnter ( Y ) for 'YES', ( N ) for 'No':\n>>> ")#if input is not entered correctly

def reset(nice,mean,name):
    nice = 0
    mean = 0
    #notice i do not reset the name variable as the same user chose to play again
    start(nice,mean,name)







if __name__ == "__main__":
    start()
