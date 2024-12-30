from Type_conv_module import input_type1 as IT1
def factorial(n):
    if n==1 or n==0 :
        return 1
    return n*factorial(n-1)

while(True):
    try:
        n= IT1(input("Enter a number: "))
        if isinstance(n,str) or isinstance(n,float) or n<0:
            print("Please enter a positive integer!")
        else:
           print(factorial(n))
    except KeyboardInterrupt:
            print("\nExiting...")
            break        