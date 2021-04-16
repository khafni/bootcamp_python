class Vector:
    def __init__(self, *args):
        if isinstance(args[0], list):
            self.list = args[0]
        elif isinstance(args[0], int):
            self.list = [0 for i in range(int(args[0]))]
        elif isinstance(args[0], range):
            self.list = [0 for i in args[0]]
        self.size = len(self.list)

    def __add__(self, v_or_s):
        r_lst = []
        if isinstance(v_or_s, float):
            for e1 in self.list:
                r_lst.append(e1 + v_or_s)
        elif isinstance(v_or_s, Vector):
            if self.size != v_or_s.size:
                raise Exception(
                    "vector addition on vectors with different dimensions")
            for e1, e2 in zip(self.list, v_or_s.list):
                r_lst.append(e1 + e2)
        r_v = Vector(r_lst)
        return r_v

    def __radd__(self, v_or_s):
        return self._add__(v_or_s)

    def __sub__(self, v_or_s):
        r_lst = []
        if isinstance(v_or_s, float):
            for e1 in self.list:
                r_lst.append(e1 - v_or_s)
        elif isinstance(v_or_s, Vector):
            if self.size != v_or_s.size:
                raise Exception(
                    "vector addition on vectors with different dimensions")
            for e1, e2 in zip(self.list, v_or_s.list):
                r_lst.append(e1 - e2)
        r_v = Vector(r_lst)
        return r_v

    def __rsub__(self, v_or_s):
        return self.__sub__(v_or_s)

    def __truediv__(self, num):
        if num == 0:
            raise Exception("dividing by 0")
        return Vector([i / num for i in self.list])

    def __rtruediv__(self, num):
        arr = []
        for n in self.list:
            if num == 0:
                raise Exception("dividing by 0")
            arr.append(num / n)
        return Vector(arr)

    def __mul__(self, v_or_s):
        r = 0
        if isinstance(v_or_s, float):
            for e1 in self.list:
                r_lst.append(e1 * v_or_s)
        elif isinstance(v_or_s, Vector):
            if self.size != v_or_s.size:
                raise Exception(
                    "Error : trying to multiply vectors with different dimensions")
            for e1, e2 in zip(self.list, v_or_s.list):
                r += e1 * e2 
        return r

    def __rmul__(self, v_or_s):
        return __mul__(self, v_or_s)
    def __str__(self):
        i = 0
        s = "{} elements floats Vector: {}".format(self.size, self.list)
        return s
    def __repr__(self):
        str = "Vector({})\n".format(self.list)
        str += self.__str__()
        return str

