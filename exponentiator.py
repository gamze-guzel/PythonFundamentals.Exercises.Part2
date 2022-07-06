def exponentiator(a,b):
    """"return x to the power of y"""
    return a**b

def raise_to_fourth_power(x):
    "return x to the 4th power"
    return x**4

square = lambda x: exponentiator(x, 2)

cube = lambda x: exponentiator(x, 3)

print(square(2))

print(cube(2))

print(raise_to_fourth_power(2))
