import sys


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Error")
        return
    for w in sys.argv:
        if not w.isalnum():
            sys.stderr.write("Error")
            return


if __name__ == "__main__":
    main()
