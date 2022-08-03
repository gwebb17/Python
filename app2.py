
import app

def print_app2():
    name = (__name__)
    return name

if __name__ == "__main__":
#the following is calling code from within this script
    print("I am running code from {}".format(print_app2()))

#the following is calling code from the imported app.py 
    print("I am running code from {}".format(app.print_app()))
#the app after .format is calling the file we want to access print_app from. 
