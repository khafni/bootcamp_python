from matrix import Matrix
from matrix import Vector


            
#mat = Matrix((8, 8))
mat1 = Matrix([[1, 1], [1, 1]])
mat2 = Matrix([[-1, -1], [-1, -1]])
mat = Matrix([[1, 2], [3, 4]]) 
#print(1 / mat)
#print(2 * mat)
""" print(mat1)
print("")
print(mat)
print("")
print(mat1 * mat)
 """
mat3 = Matrix([[0, -1, 2], [4, 11, 2]])
mat4 = Matrix([[3, -1], [1, 2], [6, 1]])
mat5 = mat3 * mat4
""" print("")
print(mat5)
 """
mat6 = Matrix([[3,2,0], [0,4,1], [2,0,1]])
v = Vector([4, 3, 1])

print(mat6 * v)