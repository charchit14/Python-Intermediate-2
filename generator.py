# Demonstration of generator (memory-efficient meethod)

# Demonstration 1
# def gen(n):
#     for i in range(n):
#         yield i

# result = gen(21)
# for i in result:
#     print(i)


# Demonstration 2 (using 'next' to generate (one at a time) )
def gen(n):
    for i in range(n):
        yield i

result = gen(21)
print(next(result))
print(next(result))
print(next(result))