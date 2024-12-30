import random

char= 'abcdefghijklmnopqrstuvwxyz!@#$%^&*()?'

# BY TRY AND EXCEPT
try:
    n_o_p = int(input("Total number of password: "))
    if n_o_p ==0:
        print("OK!")
    elif n_o_p <0:
        print("Please enter a postiver integer.")
    else:
        for i in range(n_o_p):
            length= int(input(f"Enter password({i+1}) length(limit=100000): ")) 
            if length<=0:
                print("Please enter valid length(greater than 0).")
                break
            # password=''
            # for p in range(length):
            password =''.join(random.choice(char) for _ in range(length))
            print(f"Password({i+1}) is: {password}")

except Exception as e:
    print("Please enter a valid number.")


# # BY IF-ELSE LOOP
# n_o_p = input("Total number of password: ")
# if n_o_p.isdigit():
#     n_o_p=int(n_o_p)
#     if n_o_p==0:
#         print("OK!")
#     else:
#         for i in range(n_o_p):
#             length= input(f"Enter password({i+1}) length: ")
#             if length.isdigit():
#                 length=int(length)
#                 if length==0:
#                     print("Please enter valid length.")
#                     break
#                 else:
#                     password=''
#                     for p in range(length):
#                         password += random.choice(char)
#                     print(f"Password({i+1}) is: {password}")
#             elif length.lstrip("-").isdigit():
#                 print("Please enter a positive integer.")
#                 break
#             else:
#                 input("Please enter a valid number.")
#                 break
# elif n_o_p.lstrip("-").isdigit():
#     print("Please enter a positive integer.")
    
# else:
#     print("Please enter a valid number.")
    