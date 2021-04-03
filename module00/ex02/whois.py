import sys

def main():
    if (len(sys.argv) != 2) or (not (sys.argv[1].isnumeric())):
        print("ERROR")
    else:
        if int(sys.argv[1]) % 2 == 0:
            print("I'm Even.")
        else:
            print("I'm Odd.")


if __name__ == "__main__":
    main()