class Vector:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.list = args[0]
        elif isinstance(args[0], int):
            self.list = [0 for i in range(int(args[0]))]
        elif isinstance(args[0], range):
            self.list = [0 for i in args[0]]

    def __add__(self, v_or_s):
        r = []
        if isinstance(v_or_s, int):
            for e1 in self.list:
                r.append(e1 + v_or_s)




v = Vector([4, 2, 4, 1])

v1 + v2 + v3
print(v.list)