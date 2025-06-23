import numpy as np

# arr1 = np.array([1,2,3,4,5])
# print(" 1D array:", arr1)
# print(" Shape:", arr1.shape)
# print("Dimesnion:", arr1.ndim)

# arr2 = np.array([[1,2,3], [4,5,6]])
# print("/n 2D array:/n", arr2)
# print(" Dimesnion", arr2.ndim)
# print("data type", arr2.dtype)

# zeros = np.zeros((2, 3))
# print("Zeroes Array", zeros)
# print("Shape,", zeros.shape)

# ones = np.ones((3,2))
# print("Ones array", ones)
# print("shape", ones.shape)

# arr4 = np.array([1,2,3,4,5], dtype = "str")
# print("data type", arr4.dtype)

arr5 = np.array([1,2,3,4,5,6,7,8,9])
print("shape", arr5.shape)
print("reshape", arr5.reshape(3,3))

arr6= np.arange(1,10)
print(arr6)

arr7= np.array([5, 3, 1 , 9, 7, 10])
print(np.sort(arr7,))
print(arr7[0])
