# Demonstration of *args and **kwargs

def anyFunc(normal, *args, **kwargs):

    print(normal)

    for i in args:
        print(i)

    for key,value in kwargs.items():
        print (key, value)

a = "I am walking"

list = ["apple", 18, 23]

dict = {
    "A": 0,
    "B": 1,
    "C": 2
}

anyFunc(a, *list, **dict)