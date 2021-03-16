import numpy as np

a = np.array([[0.5, -0.5], [-0.5, 1]])

print('Array a:')
print(a)
ainv = np.linalg.inv(a)

print('Inverse of a:')
print(ainv)
print(np.linalg.det(a))

# this is the solution to linear equations x = 5, y = 3, z = -2
