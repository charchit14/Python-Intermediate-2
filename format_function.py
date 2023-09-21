# Demonstration of format function

# Demonstration 1
# name = 'Lalu Yadav'
# marks = 99.99

# print("{} has scored {} marks in final exam".format(name, marks))


# Demonstration 2
players = ['Erling', 'KDB', 'Ruben', 'Ederson']
position = ['FWD', 'MID', 'DEF', 'GK']

# for i in range(0, len(players)):
#     print(players[i], "plays at", position[i])

# Using format function to print
for i in range(0, len(players)):
    print("{} plays at {}".format(players[i], position[i]))


# Demonstration 3
# for i in range(0, len(players)):
#     print("{1} plays at {0}".format(players[i], position[i]))
