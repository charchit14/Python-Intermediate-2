# Demonstration of lambda function
# Lambda function helps in defining functions in a single line

# Demonstration 1
add = lambda a,b : a+b
print(add(3,5))


# Demonstration 2
anyFunc = lambda a,b : b>a
print(anyFunc(223,4))


print()


# Demonstration 3
l = [(2,4), (0,9), (66,999), (999,-2)]

l.sort(key = lambda x:x[1])

print(l)

''' This program sorts a list of tuples based on the second element (index 1) of each tuple '''