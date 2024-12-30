# 0 1 1 2 3 5 8 13 21 34 55 


## fibonacci upto n
# Without Recursion
def fibonacci_upto_n(n):
    if(n<0):
        return ("Incorrect input")
    else:
        i,j=0,1
        list=[]
        while(i<=n):
            list.append(i)
            i,j=j,i+j
        return list
        # print(list)
# With Recursion            
def fibonacci_upto_n_rec(n,a=0,b=1):
    if(n<0):
        return ("Incorrect input")
    elif a>n:
        return []
    else:
        fib_list=[a]
        return fib_list+fibonacci_upto_n_rec(n,b,a+b)


## Nth Fibonacci
from math import sqrt
# Without Recursion
def nth_fibonacci(n):
    if n<0:
        print("Please enter a +ve integer!")
        return
    else:
        nth_fibo= (((1+sqrt(5))**n)-((1-sqrt(5))**n))/(2**n*(sqrt(5)))
        return round(nth_fibo)
# With Recursion
def nth_fibonacci_rec(n):
    if(n<=0):
        print("Incorrect input")
        return
    elif(n==0):
        return 0
    elif(n==1 or n==2):
        return 1
    else:
        nth_fibo=nth_fibonacci_rec(n-2)+nth_fibonacci_rec(n-1)
        return nth_fibo 


## Check a n to be Fibonacci
def check_if_fibonacci(n):
    if n<0:
        print("Enter a +ve integer.")
    elif n in fibonacci_upto_n(n):
        print(f"Yes {n} is a fibonacci number.")
    else:
        print(f"NO! {n} is not a fibonacci number.")
    
# nth multiple of k in Fibonacci series
def nth_mult(n,k):
    i=2
    while i!=0:
        a=nth_fibonacci(i)
        print(a,i)
        if a%k==0: #i for which this true
            b=nth_fibonacci((n*i)) # Logic-every ith element is zero (is recurring pattern) so we find nth a%k==0 element (n*i) and use it as index
            return b,a,i 
        i+=1
# k= int(input("Enter the value of k: "))
     

n = int(input("Enter the value of n: "))
print(f"Fibonacci series upto {n} is :{fibonacci_upto_n(n)}")
print(f"Fibonacci number at {n} place is: {nth_fibonacci_rec(n)}")
check_if_fibonacci(n)

        