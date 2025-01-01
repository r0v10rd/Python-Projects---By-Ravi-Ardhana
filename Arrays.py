##1.1 Method of python array
from array import array # this imports only the array class from array module so array.array is not req, just array<class> can be used
# import array # this imports the module array so to access class array, it has to be called.

# def sum_array(arr):
#     l= len(arr)
#     sum=0
#     for i in range(0,l):
#         sum+=arr[i]
#     return sum

def array_upto_n(l):
    lis= []
    for i in range(1,l+1):
        lis.append(i)
    arr = array('i',lis)
    return arr


##1.2 Method with NumPy array
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


##3.1 Array Rotation to the left
# l=int(input("Enter length of array: "))
# arr = array_upto_n(l)
# elements_to_shift = len(arr)-1
# print("Length of array: ",len(arr))
# print("Elements to be shifted: ",elements_to_shift)
# print("Initial array:",arr)
# NoR= int(input("Enter no. of rotations: "))
# for i in range(NoR):
#     a = arr[0]
#     for j in range(elements_to_shift):
        # arr[j]=arr[(j+1)]
#     print(f"Rotated Array in rotation {i+1}:", arr)
#     arr[-1]=a
# print("Rotated array:",arr)

##3.2 Array rotation to the right
# l=int(input("Enter length of array: "))
# arr = array_upto_n(l)
# elements_to_shift = len(arr)-1
# print("Length of array: ",len(arr))
# print("Elements to be shifted: ",elements_to_shift)
# print("Initial array:",arr)
# NoR= int(input("Enter no. of rotations: "))
# for i in range(NoR):
#     a = arr[elements_to_shift]
#     for j in range(0,elements_to_shift):
#         arr[elements_to_shift-j]=arr[elements_to_shift-j-1]
#     arr[0]=a
#     print(f"Rotated Array in rotation {i+1}:", arr)
# print("Rotated array:",arr) 

##3.3 Reverse an array
# l=int(input("Enter length of array: "))
# arr = array_upto_n(l)
# n = len(arr)-1
# print("Length of array: ",len(arr))
# print("Initial array:",arr)
# i=0
# while (n//2)>i:
#     arr[i],arr[n-i] = arr[n-i],arr[i]
#     i+=1
# print("Reversed Array :", arr)
 

##3.4 Split the array and add the first part to the end
# arr = [12,45,36,76,43,80,99]
# elements_to_shift = len(arr)-1
# print("Initial array:",arr)
# n= int(input("Enter elements to split: "))
# split_from= n-1
# for i in range(split_from+1):
#     a = arr[0]
#     for j in range(elements_to_shift):
#         arr[j]=arr[(j+1)]
#     arr[-1]=a
# print("Resultent array:",arr)

##4 Find remainder of array multiplication divided by n
def find_remainder(arr,n):
    l=len(arr)
    product=1
    for i in range(0,l):
        product*=arr[i]
    return product%n

arr =[45,3,57,98,10]
arr = array('i',arr)
n= 11


##5 Check if given array is Monotonic
lis =[45,3,57,98,10]
lis.sort()
arr= array('i',lis)
l = len(arr)
def isMonotonic(arr):
    for i in range(len(arr)-1): 
       return (all(arr[i]<=arr[i+1]for i in range(len(arr)-1))) or (all(arr[i]<=arr[i+1]for i in range(len(arr)-1))) # all elements should be true in an iterable for all() to return True

def isMonotonic(arr):
    is_increasing = True
    is_decreasing = True
    
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            is_increasing = False
        if arr[i] < arr[i + 1]:
            is_decreasing = False
    
    return is_increasing or is_decreasing

