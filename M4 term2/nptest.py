import numpy as np

a = np.array([[-2, 1],
            [-1, 3],
            [4, 0]])

b = np.array([[4, 1],
            [2, -3],
            [0, 3]])

c = np.array([[5, 1],
            [-1, 3],
            [2, 1]])
print(a+(b-c))