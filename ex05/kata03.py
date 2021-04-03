def main():
    phrase = "The right format"
    phrase = phrase.rjust(42, '-')
    print(phrase, end='')


if __name__ == "__main__":
    main()