# Demonstration of reduce function

from functools import reduce

def add(n1,n2):
    return n1+n2

# Using reduce function
result = reduce(add, [2,3,4,5])

print(result)

''' How does reduce function actually work?
Here, at first it adds 2 and 3 which results to 5
then it picks up the next item which is 4 and adds 4 with previous result i.e. 5
the result i.e. 9 is now added with 5 which results 14 '''