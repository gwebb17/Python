#prints out 0,1,2,3 because its going through each number from 0-4
x = range(4)
for i in x:
    print(i)

#starts at 3, goes to -1, and increments by -1 each time (3,2,1,0)
y = range(3,-1,-1)
for i in y:
    print(i)

#starts at 8 and counts down by -2 until 2
z = range(8,0,-2)
for i in z:
    print(i)
