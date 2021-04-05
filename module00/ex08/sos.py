import sys


def word_to_morse(word):
    word = word.lower()
    r_str = ""
    for x in word:
        if x == 'a':
            r_str += '.-'
        elif x == 'b':
            r_str += '-...'
        elif x == 'c':
            r_str += '-.-.'
        elif x == 'd':
            r_str += '-..'
        elif x == 'e':
            r_str += '.'
        elif x == 'f':
            r_str += '..-.'
        elif x == 'g':
            r_str += '--.'
        elif x == 'h':
            r_str += '....'
        elif x == 'i':
            r_str += '..'
        elif x == 'j':
            r_str += '.---'
        elif x == 'k':
            r_str += '-.-'
        elif x == 'l':
            r_str += '.-..'
        elif x == 'm':
            r_str += '--'
        elif x == 'n':
            r_str += '-.'
        elif x == 'o':
            r_str += '---'
        elif x == 'p':
            r_str += '.--.'
        elif x == 'q':
            r_str += '--.-'
        elif x == 'r':
            r_str += '.-.'
        elif x == 's':
            r_str += '...'
        elif x == 't':
            r_str += '-'
        elif x == 'u':
            r_str += '..-'
        elif x == 'v':
            r_str += '...-'
        elif x == 'w':
            r_str += '.--'
        elif x == 'x':
            r_str += '-..-'
        elif x == 'y':
            r_str += '-.--'
        elif x == 'z':
            r_str += '--..'
        elif x == '0':
            r_str += '-----'
        elif x == '1':
            r_str += '.----'
        elif x == '2':
            r_str += '..---'
        elif x == '3':
            r_str += '...--'
        elif x == '4':
            r_str += '....-'
        elif x == '5':
            r_str += '.....'
        elif x == '6':
            r_str += '-....'
        elif x == '7':
            r_str += '--...'
        elif x == '8':
            r_str += '---..'
        elif x == '9':
            r_str += '----.'
        r_str += ' '
    return r_str
 
def words_to_morse(words):
    l = words.split(' ')
    r_l = []
    for w in l:
        r_l.append(word_to_morse(w))
    s = " / ".join(r_l)
    return s
        


def main():
    if len(sys.argv) < 2:
        sys.stderr.write("Error")
        return
    i = 1
    while i < len(sys.argv):
        for c in sys.argv[i]:
            if (not c.isalnum()) and not c.isspace():
                sys.stderr.write("Error")
                return
        i+= 1
    i = 1
    arr = []
    while i < len(sys.argv):
        arr.append(words_to_morse(sys.argv[i]))
        i += 1  
    s = " / ".join(arr)
    s = " ".join(s.split())
    print(s)


if __name__ == "__main__":
    main()
