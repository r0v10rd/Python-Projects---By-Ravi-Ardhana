a = int(input("Enter limit: "))
interval = int(input("Enter interval: "))
def is_prime(n):
    if n ==1 or n==0:
        print("1 and 0 are neither prime nor composite.")
    else:
        for i in range(2,n-1):
            if n%i==0:
                return False
        return True
def prime_upto_n(n):
    list=[]
    for i in range(2,n):
        if is_prime(i): # can be used without ==
            list.append(i)
    return list
def prime_in_interval(n,i):
    list=[]
    e= prime_upto_n(n)
    for index,item in enumerate(e):
        if (index+1)%i==0:
            list.append(item)
    return list
print(f"List of prime numbers upto {a} is :{prime_upto_n(a)}")
print(f"List of prime numbers upto {a} in interval {interval} is : {prime_in_interval(a,interval)}")
