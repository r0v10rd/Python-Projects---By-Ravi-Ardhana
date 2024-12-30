from Type_conv_module import input_type1 as IT1
pa=IT1(input("Enter principle amount: "))
t= IT1(input("Enter time(in yrs): "))
i= IT1(input("Enter interest: "))
if isinstance(pa,str) or isinstance(i,str) or isinstance(t,str):
    print("Enter valid data.")
else:
    si=(pa*i*t)/100
    ci=pa*((1+i/100)**t-1)
    print(f"The Simple interest is:{si}")
    print(f"The Compound interest is:{ci}")
