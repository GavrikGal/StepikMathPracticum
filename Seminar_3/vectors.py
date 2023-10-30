import numpy as np

M1 = np.array((
    (1., 2., 3., 0.),
    (4., 5., 6., 0.),
    (0., 1., 1., 6.),
    (7., 8., 9., 0.)
))

def sin_x(x):
    return np.sin(x * np.pi / 6)

M1[-2] = sin_x(M1[-2])

M1[:, -2] = np.exp(M1[:, -2])

M2 = M1

# print(M2)

M = np.array((
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10]
))
# print(M.shape)

v1 = np.array((1, 2, 3))
v2 = np.array((3, 4, 5))

# print(v1.dot(v2))

v = np.array([1, 2, 3, 4, 5])

print(v.astype(float))