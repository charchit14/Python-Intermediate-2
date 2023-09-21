# Demonstration of map function

l1 = [2,3,4]
l2 = [3,2,1]

def add(a,b):
    return a+b

# Using map function to add two list
result = map(add, l1, l2)

print(list(result))


print()


# Demonstration of filter function

def greater(n):
    if n>4:
        return True
    else:
        return False

l = [3,4,1,0,-9,6,8,6]

# Using filter function
result = filter(greater,l)

print(list(result))