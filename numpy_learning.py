# Linear regression



import numpy as np

# array = np.array([[1,2,3], [2,3,4]])
#
# # print('number of dim:', array.ndim)
# # print('shape:',array.shape)
# # print('size:', array.size)
#
# a =  np.array([[1,2,3], [2,3,4], [1,2,3]])
#
# b =  np.arange(12).reshape((4,3))
#
# # 生成线段
# c = np.linspace(1,10,9).reshape((3,3))
#
#
# #
# d = np.random.random((2,4))
#
# # np.sum(a)
# # row
# # np.min(a, axis = 0)
# # column
# # np.max(a, axis = 1)
#
# # matrix with bools
# print(b<3)
#
#
# # matrix mult
# m_mul = np.dot(b,c)
# m_mul2 = b.dot(c)
#
# # paar multi
# i_mul = a*c
#
#
# print(m_mul)
# print(i_mul)
# print(m_mul2)


# 14~2 step: -1
# A = np.arange(14,2,-1).reshape((3,4))

# to find the index of
# print(np.argmin(A))

# mean average value

# cumsum iterate additive, same shape
# diff : iterate sub

# A.T transport np.transpose

# np.clip(A,5,9)
# all the number <5 := 5,  >9 :=9, otherwise = self

# A[2, :]
#  all the numbers in 3. row

# A[1, 1:3]
#  1-3 numbers in second row

# A.flatten() generate for each item


# A = np.array([1,1,1])[:, np.newaxis]
# B = np.array([2,2,2])[:, np.newaxis]
#
# print(np.vstack((A,B))) # vertical stack
#
# print(np.hstack((A,B))) # horizontal stack
#
# C = np.concatenate((A,B,B,A), axis=0)

A = np.arange(12).reshape((3,4))

D = np.vsplit(A,3)
E = np.hsplit(A,4)

print(A)
print(D)
print(E)
