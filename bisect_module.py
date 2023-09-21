# Demonstration of bisect module

import bisect

l = [2, 3, 5, 6, 8, 12, 14, 16, 21]

num = 4 
# Insert 4 in such a way that the list remains sorted

# Use of bisect module
print(bisect.bisect(l, num))    # Gives us the index where we need to insert the number to keep the list sorted

# This will actually insert the number and give us the list
bisect.insort(l, num)
print(l)

''' NOTE: bisect module won't check if the list is sorted or not.
So, we need to make sure that the list is sorted '''