def largest(list):
    # list=map(int,list)
    max = list[0]
    length= len(list)
    for i in range(1,length):
        if list[i]>max:
            max = list[i]
    return max
n = int(input("Enter length of list:"))
list = []
for i in range(0,n):
    element =int(input(f"Enter element no.{i+1}: "))
    list.append(element)
print(f"The maximum number in the list= {list} is: {largest(list)}")