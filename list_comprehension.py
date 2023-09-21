# Demonstration of list comprehension

# For a given list WAP to print the numbers that are divisible by 5

# Program 1 (without using list comprehension)
list = [2, 5, 0, 4, 7 , 63, 55]
result = []
for i in list:
    if i%5==0:
        result.append(i)
print(result)


# Program 2 (using list comprehension)
list = [2, 5, 0, 4, 7 , 63, 55]
result = [i for i in list if i%5==0]
print(result)