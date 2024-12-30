##1 Method of python array
from array import array # this imports only the array class from array module so array.array is not req, just array<class> can be used
# import array # this imports the module array so to access class array, it has to be called.

# def sum_array(arr):
#     l= len(arr)
#     sum=0
#     for i in range(0,l):
#         sum+=arr[i]
#     return sum

# def array_upto_n(l):
#     lis= []
#     for i in range(1,l+1):
#         lis.append(i)
#     arr = array('i',lis)
#     return arr


##1.1 Method with NumPy array
import numpy as np
def create_array(l):
    lis=[]
    for i in range(1,l+1):
        n = int(input(f"Enter element no.{i}: "))
        lis.append(n)
    arr = np.array(lis)
    return arr

def sum_array(arr):
    l= len(arr)
    sum=0
    for i in range(0,l):
        sum+=arr[i]
    return sum


##2 Largest element in array
def largest_element(arr):
    max=arr[0]
    l= len(arr)
    for i in range(1,l):
        if max<arr[i]:
            max=arr[i]
    return max

l= int(input("Enter length of array: "))
arr = create_array(l)
print(arr)
print(largest_element(arr))