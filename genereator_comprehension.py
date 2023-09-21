# Demonstration of generator comprehension

g = (i for i in range(8) if i%2==0)
print(g)
for i in g:
    print (i)