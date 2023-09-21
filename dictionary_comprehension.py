# Demonstration of dictionary comprehension

# Squaring the values of key for each key in dictionary
d = {
    'a': 20,
    'b': 30,
    'A': 40
    }

result = {key:value**2 for key,value in d.items()}
print(result)