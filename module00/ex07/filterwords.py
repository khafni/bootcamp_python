import sys

def main():
    punc = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    print(sys.argv[1])
    if len(sys.argv) != 3 or sys.argv[1].isdigit() or not sys.argv[2].isdigit():
        sys.stderr.write("ERROR")
        return
    strs = sys.argv[1]
    for c in strs:
        if c in punc:
            strs = strs.replace(c, '')
    strs = strs.split(' ')
    l = int(sys.argv[2])
    strs = [s for s in strs if len(s) > l]
    print(strs)

if __name__ == "__main__":
    main()
