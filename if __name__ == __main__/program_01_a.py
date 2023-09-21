import os

def anyFunc():
    print("What you lookin' at?")

print(__name__)

if __name__ == "__main__":
    print(os.listdir())
    print("Where is this line?")

''' Note: Whenever we import one program in other program, all of its contents will be imported in other program
and hence, everything in host program will be printed. So, we use __name__ == "__main__" in host program '''

''' Putting things inside __name__ == "__main__ " will print everything in this program
but if this program is imported in another program then whatever the other program calls only that will run
which means contents inside __name__ == "__main__" won't run in the other program '''

''' print(__name__) --> This will print __main__ in this program because the 'name' is 'main' here (since, it is the host program)
But in 'program_01_b', it will print 'program_01_a' because 'program_01_b' is imported from 'program_01_a' '''