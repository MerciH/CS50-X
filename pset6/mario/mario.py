from cs50 import get_int


def main():

    height = 0
    #promt again if h is out of range
    while 1 > height or height > 8:
        height = get_int("Height: ")

    #print
    for i in range(0, height):

        for j in range(0, height-i-1):
            print(" ", end="")

        for k in range(0, i+1):
            print("#", end="")

        print("  ", end="")

        for l in range(0, i+1):
            print("#", end="")
        print()

main()


