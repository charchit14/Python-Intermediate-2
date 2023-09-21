import os

def anyFunc():
    print("What you lookin' at?")

print(__name__)

def main():
    print(os.listdir())
    print("Where is this line?")
    anyFunc()

if __name__ == "__main__":
    main()


''' Suppose, in the imported program i.e. 'program_02_b' we want to print other contents along with the called function
we use 'main()' and whenever 'main()' is called in 'program_02_b' the contents inside 'main()' will be printed '''