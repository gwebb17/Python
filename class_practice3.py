class BabyGrand:
    def __init__(self, Keys, Pedals, Year_Built, Condition):
        self.Keys = Keys
        self.Pedals = Pedals
        self.Year_Built = 1919
        self.Condition = "Good"

#needs to be same indent as parent class otherwise won't recognize method outside class
def display():
        print("\nBaby Grand Pianos have {} Keys".format(babygrand.Keys))


babygrand = BabyGrand(88, 3, 1919, "Good")

class Kawai(BabyGrand):
    Year_Built = 2015
    Condition = "Excellent"
    Model = "ES-8"

objES8 = Kawai(88, 3, 2015, "Good")

def display2():
    print("\nKawai model is called the {}".format(objES8.Model))





if __name__ == "__main__":
    print(babygrand.Keys)
    print(babygrand.Year_Built)
    display()
    display2()
  
