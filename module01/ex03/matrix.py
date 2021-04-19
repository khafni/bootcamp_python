from vector import Vector
# reverse magic methods aren't implemented for commutative operations 
class Matrix:
    def __init__(self, mat_or_shape):
        if isinstance(mat_or_shape, list):
            if not self.check_if_valid_mat(mat_or_shape):
                raise Exception("trying to construct an invalid matrix")
            self.data = mat_or_shape
            self.shape = (len(mat_or_shape), len(mat_or_shape[0]))
        elif isinstance(mat_or_shape, tuple):
            if len(mat_or_shape) != 2:
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
        m1 = self
        if isinstance(m_or_s, float) or isinstance(m_or_s, int):
            mat = Matrix((self.shape[0], self.shape[1]))
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    mat.data[i][j] = self.data[i][j] * m_or_s
            return mat
        elif isinstance(m_or_s, Matrix):
            m2 = m_or_s
            mat = Matrix((m1.shape[0], m_or_s.shape[1]))
            if m1.shape[1] != m2.shape[0]:
                raise Exception("matrix multiplication error:\n M1 * M2 can't be done since M1 num of columns != M2 number of rows")
            for i in range(mat.shape[0]):
                for j in range(m2.shape[1]):
                    for k in range(m2.shape[0]):
                        mat.data[i][j] += m1.data[i][k] * m2.data[k][j] 
            return mat
        elif isinstance(m_or_s, Vector):
            if self.shape[1] != m_or_s.size:
                raise Exception("matrix vector multiplication error:\n M1 * v1 can't be done since M1 num of columns != v1 size")
            mat = Matrix((self.shape[0], 1))
            for i in range(mat.shape[0]):
                for k in range(m_or_s.size):
                    mat.data[i][0] += self.data[i][k] * m_or_s.list[k]
            return mat
        return 1

    def __rmul__(self, m_or_s):
        m = self
        if isinstance(m_or_s, float) or isinstance(m_or_s, int):
            mat = Matrix((self.shape[0], self.shape[1]))
            for i in range(mat.shape[0]):
                for j in range(mat.shape[1]):
                    mat.data[i][j] = self.data[i][j] * m_or_s
            return mat
        elif isinstance(m_or_s, Matrix):
            m1 = m_or_s
            m2 = self
            mat = Matrix((m1.shape[0], m_or_s.shape[1]))
            if m1.shape[1] != m2.shape[0]:
                raise Exception("matrix multiplication error:\n M1 * M2 can't be done since M1 num of columns != M2 number of rows")
            for i in range(mat.shape[0]):
                for j in range(m2.shape[1]):
                    for k in range(m2.shape[0]):
                        mat.data[i][j] += m1.data[i][k] * m2.data[k][j]
            return mat

       