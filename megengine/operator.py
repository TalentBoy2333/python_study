import megengine as mge
import megengine.functional as F

A = mge.tensor([[2., 4., 2.],
                [2., 4., 2.]])
B = mge.tensor([[1., 2., 1.],
                [1., 2., 1.]])

print(A + B)
print(A - B)
print(A * B)
print(A / B)

print(F.add(A, B))
print(F.sub(A, B))
print(F.mul(A, B))
print(F.div(A, B))

A = mge.tensor([[1., 2., 3.],
                [4., 5., 6.]])

print(A[1, :2])

A = mge.tensor([[1., 2., 3.],
                [4., 5., 6.]])

print(A.shape)
A = A.reshape(3, 2)
print(A.shape)

x = mge.tensor([[1., 3., 5.],
                [2., 4., 6.]])
w = mge.tensor([[1., 2.],
                [3., 4.],
                [5., 6.]])

p = F.matmul(x, w)
print(p)