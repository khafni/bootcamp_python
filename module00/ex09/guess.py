import sys
import random

def main():
    rn = random.randint(0, 101) 
    n_attempts = 0
    while True:
        str = input("What's your guess between 1 and 99?")
        if str == "exit":
            print("Goodbye!")
            break
        n = int(str)
        if (n < rn):
            print("Too low!")
            n_attempts += 1
        elif (n > rn):
            print("Too high!")
            n_attempts += 1
        else:
            print("Congratulations, you've got it!")
            print("You won in {} attempts!".format(n_attempts))
            break


if __name__ == "__main__":
    main()
