import numpy as np
a = np.array([1,2,3,4,5]) 
print(a)
print(np.__version__)

arr = np.array(12)
arr1 = np.array([1,2,3,4,5,6])
arr2 = np.array([[1,2,3],[4,5,6]])
arr3 = np.array([[[1,2,3],[4,5,6]],[[1,2,3],[4,5,6]]])
print(arr.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

az =np.array([1,2,3,4],ndmin=5)
print(az)
print("The number of dimension:",az.ndim)