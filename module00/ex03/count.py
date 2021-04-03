import sys

def text_analyzer(*text):
    if len(text) > 1:
        print("ERROR")
        return
    if len(text) == 0:
        print ("please enter a text!")
        return
    upp_ls = 0
    low_ls = 0
    puncts_marks = 0
    spaces = 0
    for c in text[0]:
        if c.isupper():
            upp_ls += 1
        elif c.islower():
            low_ls += 1
        elif c == ' ':
            spaces += 1
        elif c in "',.?!;:`-":
            puncts_marks += 1
    print("The text contains {} characters:".format(len(text[0])))
    print("- {} upper letters".format(upp_ls))
    print("- {} lower letters".format(low_ls))
    print("- {} punctuation marks".format(puncts_marks))
    print("- {} spaces".format(spaces))


def main():
    text_analyzer("425224 rand ,.!? ")

if __name__ == "__main__":
    main()