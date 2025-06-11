#Joins in numpy

import numpy as np

arr1 = np.array([1,2,3])
arr2 = np.array([4,5,6])
arr3 = np.concatenate((arr1,arr2))
print(arr3)

arr1 = np.array([[1,2],[3,4]])
arr2 = np.array([[5,6],[7,8]])
arr3 = np.concatenate((arr1,arr2),axis=1)
print(arr3)

fname = input("Enter your first name:")
fname1 = np.array([fname])
lname = input("Enter your last name:")
lname1 = np.array([lname])
##print(fname1)
##print(lname1)
cat = np.concatenate((fname1,lname1))
print(cat)
