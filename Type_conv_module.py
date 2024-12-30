def input_type1(a):
    try:
        str_a = str(a)
        # in can be used for str values only
        return float(a) if '.' in str_a else int(a)
    except ValueError:
        return str(a)

def input_type2(a, b):
    res_a=input_type1(a)
    res_b=input_type1(b)
    return res_a,res_b

def input_type3(a,b,c):
    res_a=input_type1(a)
    res_b=input_type1(b)
    res_c=input_type1(c)
    return res_a,res_b,res_c
    