import sys

def reverse(str):
    def reverse_string():
        nonlocal str
        str = str[::-1]
    def reverse_case():
        nonlocal str
        for i in range(len(str)):
            if str[i].isupper():
                str = str[:i] + str[i].lower() + str[i + 1:]
            else:
                str = str[:i] + str[i].upper() + str[i + 1:] 
    reverse_string()
    reverse_case()
    return (str)
    
    
def main():
    if len(sys.argv) >= 2:
        sys.argv = sys.argv[1:]
        result = " ".join(map(reverse, sys.argv))
        print(result)
    else:
        print(" ")


if __name__ == "__main__":
    main()