# Demonstration of kwargs

def anyFunc(**kwargs):
    for key, value in kwargs.items():
        print(key, value)

std = {
    "Katy": 56,
    "Betty": 66,
    "Cety": 76
    }

anyFunc(**std)