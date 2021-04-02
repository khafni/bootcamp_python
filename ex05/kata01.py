def main():
    languages = {
        'Python': 'Guido van Rossum',
        'Ruby': 'Yukihro Matsumto',
        'PHP': 'Rasmus Lerdorf',
    }

    for key, value in languages.items():
        print("{} was created by {}".format(key, value))

if __name__ == "__main__":
    main()