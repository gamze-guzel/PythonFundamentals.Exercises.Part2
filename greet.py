def greet(name):
    print("Hello " +name)

def name_input():
    print("What's your name?")
    name=input()
    return name
greet(name_input())

