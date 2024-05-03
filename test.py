import numpy as n
arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]
arr3 = [9, 10, 11, 12]

narr1 = n.array(arr1)
narr2 = n.array(arr2)
narr3 = n.array(arr3)

concatenated_array = n.concatenate((narr1, narr2, narr3))
stacked_array = n.vstack((narr1, narr2, narr3))
print(concatenated_array)
print(stacked_array)


list1 = [2, 3, 'asdf', {"d": 2}]
list2 = [2.33, 2.00, 5234, 233]
list1.extend(list2)
print(list1)
print("page:", arr3[-1])

