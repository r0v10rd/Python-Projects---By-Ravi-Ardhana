# Array rotation
list = [1,2,3,4,5,6,7]
NoR= int(input("Enter no. of rotations: "))
n = len(list)
index=0

# Rotated list
# if NoR==n:
#     print(f"Ye le teri rotated list: {list}")
# elif NoR>n:
#     NoR=NoR-n
#     while NoR>0:
#         a= list.pop(0) #pop takes index as arg
#         list.append(a)
#         NoR-=1
#     print(f"lelo:{list}")
# else:
#     while NoR>0:
#         a= list.pop(0) #pop takes index as arg
#         list.append(a)
#         NoR-=1
#     print(list)

# Reverse
# while index<n//2:
#     # a= list[index]
#     # list[index]=list[n-index-1]
#     # list[n-index-1]=a 
#     list[index], list[n-index-1]= list[n-index-1],list[index]
#     index+=1
# print(list)