def main():
    i = (3,30,2019,9,25)
    print("{3:02}/{4:02}/{2} {0:02}:{1:02}".format(*i))
if __name__ == "__main__":
    main()