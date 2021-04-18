
# reverse magic methods aren't implemented for commutative operations 
class Matrix:
    def __init__(self, mat_or_shape):
        if isinstance(mat_or_shape, list):
            if not self.check_if_valid_mat(mat_or_shape):
                raise Exception("trying to construct an invalid matrix")
            self.data = mat_or_shape
            self.shape = (len(mat_or_shape), len(mat_or_shape[0]))
        elif isinstance(mat_or_shape, tuple):
            if len(mat_or_shape) != 2 or mat_or_shape[0] != mat_or_shape[1]:
                raise Exception(("wrong matrix dimensions"))
            self.data = [[0 for j in range(mat_or_shape[1])] for i in range(mat_or_shape[0])]
            self.shape = mat_or_shape

    def check_if_valid_mat(self, mat_or_shape):
        zth_e_l = len(mat_or_shape[0]) #the len of the first row
        for row in mat_or_shape:
            if (len(row) != zth_e_l):
                return False
        return True

    def __str__(self):
            r_str = ""
            for row in self.data:
                r_str += str(row)
                r_str += '\n'
            r_str = r_str[:len(r_str) - 1]
            return r_str

    def __add__(self, mat1):
        if not isinstance(mat1, Matrix):
            raise Exception("you can't add a non matrix to matrix")
        if self.shape != mat1.shape:
            raise Exception("Two matrices must have an equal number of rows and columns to be added")
        mat = Matrix((self.shape[0], self.shape[1]))
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                mat.data[i][j] = self.data[i][j] + mat1.data[i][j]
        return mat

    def __sub__(self, mat1):
        if not isinstance(mat1, Matrix):
            raise Exception("you can't add a non matrix to matrix")
        if self.shape != mat1.shape:
            raise Exception("Two matrices must have an equal number of rows and columns to be substracted")
        mat = Matrix((self.shape[0], self.shape[1]))
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                mat.data[i][j] = self.data[i][j] - mat1.data[i][j]
        return mat

    def __truediv__(self, scal):
        if scal == 0:
            raise Exception("you can't divide on 0")
        mat = Matrix((self.shape[0], self.shape[1]))
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                mat.data[i][j] = self.data[i][j] / scal 
        return mat

    def __rtruediv__(self, scal):
        mat = Matrix((self.shape[0], self.shape[1]))
        for i in range(mat.shape[0]):
            for j in range(mat.shape[1]):
                if self.data[i][j] == 0:
                    raise Exception("you can't devide by 0")
                mat.data[i][j] = scal / self.data[i][j] 
        return mat

    def __mul__(self, m_or_s):
        mat = Matrix((self.shape[0], self.shape[1]))
        if isinstance(m_or_s, float) or isinstance(m_or_s, int):
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    if self.data[i][j] == 0:
                        raise Exception("you can't devide by 0")
                    mat.data[i][j] = self.data[i][j] * m_or_s
            return mat
        elif isinstance(m_or_s, Matrix):
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    if self.data[i][j] == 0:
                        raise Exception("you can't devide by 0")
                    mat.data[i][j] = self.data[i][j] * m_or_s[i][j] 
            return mat
