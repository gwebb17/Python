def typeSomething():
    val1 = input("\nType either red or blue:     ")
    val2 = input("\nType either white or black:     ")
    return val1, val2

def colorFunction():
    go = True
    while go: #while go is true do below, which is always until correct input
        val1, val2 = typeSomething()
        try:
            go = False
        except ValueError as f:
            print("{}: You didn't listen".format(f))
        finally:
            print("I give up")
    print("Good job, you typed {} and {}".format(val1, val2))


if __name__ == "__main__":
          colorFunction()
