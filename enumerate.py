# Demonstration of emumerate function

# enumerate keeps track of both items and their respective index

a = ['Zebra', 'Hippo', 73, 'Yellow', 69]

# for index, item in enumerate(a):
#     print(index,item)

for index, item in enumerate(a):
    if (index+1) % 2 ==0:
        print(index, item)