from Type_conv_module import input_type1 as IT1
def power(x, y):
    a=IT1(x)
    b=IT1(y)
    if isinstance(a,str) or isinstance(b,str):
        return 'Invalid Input'

    if b == 0:
        return 1
    if b % 2 == 0:
        return power(a, b // 2)**2
    return a * power(a, b // 2)**2