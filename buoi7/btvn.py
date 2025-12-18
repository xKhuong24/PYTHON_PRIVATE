#import numpy as np

#print(np.__version__)


#from importlib.metadata import version
#print(version('numpy'))

#import pkg_resources
#print(pkg_resources.get_distribution('numpy').version)

# Câu 2:Tạo mảng 1 chiều từ 0 đến 20
import numpy as np
arr = np.arange(21)
print(arr)

# câu 3: Tạo một mảng boolean 3x3 với tất cả giá trị là True và in ra mảng đó
import numpy as np
a = np.full((3,3), True)
print(a)

# câu 4 : Lấy những phần tử mà thoả mãn một điều kiện cho trước của mảng một chiều

import numpy as np

# tạo mảng một chiều từ 0 đến 9
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)

# Tìm phần tử có giá trị lẻ
arr_odd = arr[arr %2==1]
print(arr_odd)

# câu 5 : Thay thế phần tử thoả mãn điều kiện cho trước bằng 1 một giá trị khác

import numpy as np

# tạo mảng một chiều từ 0 đến 9
arr = np.array([0,1,2,3,4,5,6,7,8,9])
print(arr)
# Thay thế phần tử có giá trị lẻ bằng -1
arr[arr % 2 != 0] = -1
print(arr)

#6

import numpy as np
arr = np.arange(0,10)
print(arr)
arr_new = np.where(arr % 2 != 0, -1, arr)
print(arr_new)
print(arr)

#7
import numpy as np

arr = np.random.randint(0, 100, 10)
print(arr)

arr_2d = arr.reshape(2,-1)
print(arr_2d)

#8

import numpy as np

arr1 = np.arange(10).reshape(2,-1)
print('arr1: \n', arr1)
# tạo mảng hai chiều 2x5(1)
arr2 = np.ones((2,5))
print('arr2: \n',arr2)

# Cách 1 :
c = np.vstack((arr1, arr2))
print("Cách 1: \n", c)

# Cách 2 :
d = np.concatenate((arr1, arr2), axis = 0)
print("Cách 2: \n", d)

# Cách 3 :
e = np.r_[arr1, arr2]
print("Cách 3 \n",e)

#9

import numpy as np

arr1 = np.arange(10).reshape(2,-1)
print('arr1: \n', arr1)
arr2 = np.ones((2,5))
print('arr2: \n',arr2)
# Cách 1:
c = np.hstack((arr1, arr2))
print("Cách 1: \n", c)

# Cách 2:
d = np.concatenate((arr1, arr2), axis=1)
print("Cách 2: \n", d)

# Cách 3:
e = np.c_[arr1, arr2]
print("Cách 3: \n",e)

#10
import numpy as np

# chỉ dùng hàm numpy có sẵn với mảng arr như bên dưới
arr = np.array([1,2,3])
print(arr)

# tạo mảng mới lặp lại mỗi phần tử trong arr 3 lần
arr_new = np.repeat(arr, 3)
print(arr_new)

# tạo mảng mới lặp lại mảng arr 3 lần
arr_new2 = np.tile(arr, 3)
print(arr_new2)

# tạo mảng mới lặp lại mảng arr 3 lần theo chiều ngang
arr_new3 = np.tile(arr, (1, 3))
print(arr_new3)

#11
import numpy as np

a = np.array([1,2,3,2,3,4,3,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Lấy phần tử chung của 2 mảng a và b
print(np.intersect1d(a, b))

#12
import numpy as np

a = np.array([1,2,3,4,5])
b = np.array([5,6,7,8,9])

# Từ mảng a xoá tất cả các phần tử ở a mà đã có trong mảng b
print(np.setdiff1d(a, b))

#13

import numpy as np

a = np.array([1,2,3,2,3,4,3,4,5,6])
b = np.array([7,2,10,2,7,4,9,4,9,8])

# Lấy tất cả vị trí nơi giá trị các phần tử của 2 mảng a,b giống nhau
print(np.where(a == b))

#14
import numpy as np

a = np.array([2,6,1,9,10,3,27])

# tìm tất cả các phần tử có giá trị trong phạm vi [5,10]

# Cách 1:
index = ((a >= 5) & (a <= 10))
print("Cách 1: \n", a[index])

#Cách 2 : cho các bạn một phương thức khác để tìm vị trí
index = np.logical_and(a >= 5, a <= 10)
print("Cách 2: \n", a[index])

# câu 15a : Tạo hàm xử lý trên mảng numpy

import numpy as np

def maxx(x,y):
    return x if x > y else y
    # Lấy số lớn nhất nhất trong 2 số

a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])

# So sánh các cặp phần tử trong mảng a và b (theo index) sau đó lấy ra giá lớn hơn trong từng cặp
# dùng numpy.vectorize lấy hàm maxx: x,y và biến nó thành maxx: a[] -> b[].
pair_max = np.vectorize(maxx)
print(pair_max(a,b))

# câu 15b

import numpy as np

# lấy giá trị lớn hơn giữa a và b
a = np.array([5,7,9,8,6,4,5])
b = np.array([6,3,4,8,9,7,1])

# dùng hàm maximum để
maxx = np.maximum(a, b)
print("Dùng maxnimum: ", maxx)

# # dùng hàm where
where = np.where(a > b, a, b)
print("Dùng where:    ", where)

# câu 16

import numpy as np

# cho mảng arr có shape 3x3
arr = np.arange(9).reshape(3,3)
print(arr)
# Hoán cột có index 0 và index 1 trong mảng arr
print(arr[:,[1, 0, 2]])

# câu 17 :  Hoán 2 hàng trong mảng 2 chiều

import numpy as np

# cho mảng arr có shape 3x3
arr = np.arange(9).reshape(3,3)
print(arr)

#  Hoán dòng có index 0 và index 1 trong mảng arr
arr = arr[[1, 0, 2],:]
print(arr)

# câu 18 :

import numpy as np

# cho mảng arr có shape 3x3
arr = np.arange(9).reshape(3,3)
print(arr)
# Đảo ngược hàng (dòng) trong mảng 2 chiều

print(arr[::-1, :])

# câu 19

import numpy as np

# cho mảng arr có shape 3x3
arr = np.arange(9).reshape(3,3)
print(arr)

# Đảo ngược cột trong mảng 2 chiều

print(arr[:, ::-1])

# Câu 20 :  Tạo mảng 2 chiều chứa số random kiểu float từ 5 đến 10

import numpy as np


# Tạo mảng 2 chiều 5x3 từ 5 đến 10
# Cách Dùng hàm random.uniform

arr = np.random.uniform(5, 10, (5, 3))
print(arr)