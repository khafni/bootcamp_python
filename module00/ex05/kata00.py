def main():
    t = (19,42,21)
    print("the {} numbers are: {},{},{}".format(len(t), *t))
if __name__ == "__main__":
    main()