from Type_conv_module import input_type1 as IT1
def Is_Armstrong(N):
    N=IT1(N)
    y=len(str(N))    
    sum=0
    if isinstance(N,int):
        Number=N
        while(Number!=0):
            x=Number%10
            Number=Number//10
            sum=sum+pow(x,y)
        if N==sum:
            return f"{N} is an Armstrong number!"
        else:
            return f"{N} is not an Armstrong number."
    else:
        return"Enter a valid (+ve) number"
N=input("Enter a number: ")
print(Is_Armstrong(N))



