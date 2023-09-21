# Demonstration of args

# def anyFunc(name, age, roll):
#     print(f"Name is: {name}\nAge is: {age}\nRoll is: {roll}")

# anyFunc("Shark", 99, 1)


# Demonstration 1
# def anyFunc(*args):
#     print("Name is: ",args[0], "\nAge is: ",args[1], "\nRoll is: ",args[2])

# anyFunc("Shark", 99, 1)


# Demonstration 2
# def anyFunc(*args):

#     if len(args) == 3:
#         print("Name is: ",args[0], "\nAge is: ",args[1], "\nRoll is: ",args[2])
#     else:
#         print(f"Name is: {args[0]} \nAge is: {args[1]}")

# #anyFunc("Shark", 99, 1)
# anyFunc("Shark", 99)


# Demonstration 3
# def anyFunc(*args):
#         # print(f"Name is: {args[0]} \nAge is: {args[1]}")
#         print(*args)

# list = ["Crow", 66, "Raven", 666]
# anyFunc(*list)