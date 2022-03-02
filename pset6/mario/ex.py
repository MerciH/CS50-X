from cs50 import get_int

def main():

    while True:
        h = get_int("Height:")
        if 0 < h < 9:
            break

    for i in range(h):
        for j in range(h):
            if i+j < h-1:
                print(" ", end="")
            else:
                print("#", end="")
        for k in range(h):
            if i > k + 1:
                print("#", end="")
        
        print()


main()