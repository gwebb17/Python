arrizle = ['Drow', 'Slark', 'Wraith King']
arrizle2 = ['Dazzle', 'Warlock', 'Lich']


def arrizleFunction():
    x = input('type a hero')
    if x == 'Drow':
        print('Drow')
    elif x == 'Dazzle':
        print('Dazzle')
    else:
        print('Neither Drow nor Dazzle')

print("Type either {}".format(arrizle[0]))
print(" or {}".format(arrizle2[0]))

arrizleFunction()
      
