import os
import time

source = 'C:/Users/Machine/Documents/GitHub/Python/Script_Assignment/'
files = os.listdir(source)

#print directory files this is the more efficient way of doing below hardcode in one block
#the below block achieves the basic goal without hardcoding
for x in files:
    if x.endswith(".txt"):
        print(os.path.join(source, x))
        path = os.path.join(source, x)
        mTime = os.path.getmtime(path)
        print(x + " modtime: " + str(mTime))#str converts float modtime to string can't use floats

#join to absolute path name
pathA = 'test_file1.txt'
pathB = 'C:\\Users\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathC = os.path.join(pathB, pathA)
print(pathC)

pathD = 'test_file2.txt'
pathE = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathF = os.path.join(pathE, pathD)
print(pathF)

pathG = 'test_file3.txt'
pathH = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathI = os.path.join(pathH, pathG)
print(pathI)

pathJ = 'test_file4.txt'
pathK = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathL = os.path.join(pathK, pathJ)
print(pathL)

pathM = 'test_file5.txt'
pathN = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathO = os.path.join(pathN, pathM)
print(pathO)

pathP = 'test_file6.txt'
pathQ = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathR = os.path.join(pathQ, pathP)
print(pathR)

pathS = 'test_file7.txt'
pathT = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathU = os.path.join(pathT, pathS)
print(pathU)

pathV = 'test_file8.txt'
pathW = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
pathX = os.path.join(pathW, pathV)
print(pathX)

pathY = 'test_file9.txt'
pathZ = 'C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment'
path1 = os.path.join(pathZ, pathY)
print(path1)

#realizing preliminary path is already defined..
path2 = 'test_file10.txt'
path3 = os.path.join(pathZ, path2)
print(path3)



#NEXT SECTION FOR DATE/TIME
#similar setup only returning last modification time with getmtime
timeA = pathC
timeB = os.path.getmtime(pathA)
print("\n1st file last modification:", timeB)
#convert to local time
localTimeA = time.ctime(timeB)
print("1st file has last been accessed(Local time):", localTimeA)

#2
timeC = pathF
timeD = os.path.getmtime(pathD)
print("\n2nd file last modification:", timeD)
localTimeB = time.ctime(timeD)
print("2nd file has last been accessed(Local time):", localTimeB)

#3
timeE = pathI
timeF = os.path.getmtime(pathG)
print("\n3rd file last modification:", timeF)
localTimeC = time.ctime(timeF)
print("3rd file has last been accessed(Local time):", localTimeC)

#4
timeG = pathL
timeH = os.path.getmtime(pathJ)
print("\n4th file last modification:", timeH)
localTimeD = time.ctime(timeH)
print("4th file has last been accessed(Local time):", localTimeD)

#5
timeI = pathO
timeJ = os.path.getmtime(pathM)
print("\n5th file last modification:", timeJ)
localTimeE = time.ctime(timeJ)
print("5th file has last been accessed(Local time):", localTimeE)

#6
timeK = pathR
timeL = os.path.getmtime(pathP)
print("\n6th file last modification:", timeL)
localTimeF = time.ctime(timeL)
print("6th file has last been accessed(Local time):", localTimeF)

#7
timeM = pathU
timeN = os.path.getmtime(pathS)
print("\n7th file last modification:", timeN)
localTimeG = time.ctime(timeN)
print("7th file has last been accessed(Local time):", localTimeG)

#8
timeO = pathX
timeP = os.path.getmtime(pathV)
print("\n8th file last modification:", timeP)
localTimeH = time.ctime(timeP)
print("8th file has last been accessed(Local time):", localTimeH)

#9
timeR = path1
timeS = os.path.getmtime(pathY)
print("\n9th file last modification:", timeS)
localTimeI = time.ctime(timeS)
print("9th file has last been accessed(Local time):", localTimeI)

#10
timeT = path3
timeU = os.path.getmtime(path2)
print("\n10th file last modification:", timeU)
localTimeJ = time.ctime(timeU)
print("10th file has last been accessed(Local time):", localTimeJ)










#function to print txt contents of files max arguments are 8
"""def contentFunction():
    with open('test_file1.txt', 'test_file2.txt', 'test_file3.txt', 'test_file4.txt', 'test_file5.txt', 'test_file6.txt', 'test_file7.txt', 'r') as f:
        content = f.read()
        print(content)
        f.close()"""

"""
def melvillesFunction():
    for x in os.listdir():
        if x.endswith(".txt"):
            print(content)
            """

"""
path = "C:\\Users\\Machine\\Documents\\GitHub\\Python\\Script_Assignment"
dir_list = os.listdir(path)
print(dir_list)"""







"""if __name__ == "__main__":"""
    
    
