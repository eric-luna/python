""" A Functional Breakfast """

def mix_and_cook():
    print('Mixing the ingredients')
    print('Pouring the mixture into a frying pan')
    print('Cooking the first side')
    print('Flipping it!')
    print('Cooking the other side')

def make_omelette():
    mix_and_cook()
    omelette = 'a tasty omelette'
    return omelette

def make_pancake():
    mix_and_cook()
    pancake = 'a tasty pancake'
    return pancake

# make two omelettes
omelette1 = make_omelette()
omelette2 = make_omelette()

print(omelette1)
print(omelette2)
