from Type_conv_module import input_type1 as IT1
from Type_conv_module import input_type2 as IT2
a = (input("Enter NO1:"))
b = (input("Enter NO2:"))
result_a,result_b=IT2(a,b)

if isinstance(result_a,str) or isinstance(result_b,str):
    print("Enter valid numbers")
elif result_a>result_b:
    print(f"{a} is greater than {b}")
else:
    print(f"{b} is greater than {a}")
    
    