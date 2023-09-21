# Demonstration of exception handling in python
# Use of try, except, else for exception handling


# Demonstration 1
# try:
#     #print(4/2)
#     print(2/0)

# except:
#     print("Division not possible")

# else:
#     print("Division possible")

# print("Hello Guys")


# Demonstration 2
try:
    f = open("any.txt", "r")
    print(4/0)
    # print(8)

except FileNotFoundError:
    print("Error number 1")

except:
    print("Error number 2")

else:
    print("Everything Okay")

finally:
    print("This should always be printed")