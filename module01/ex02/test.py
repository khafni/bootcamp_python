from vector import Vector

def main():
    print(Vector([42 , 21, 1337]))
    print(Vector(5))
    print(Vector(range(8)))
    print(Vector([1, 2, 3]) + Vector([2, 3, 4]))
    print(Vector([1, 2, 3]) + 3)
    print(Vector([1, 2, 3]) - Vector([2, 3, 4]))

if __name__ == "__main__":
    main()