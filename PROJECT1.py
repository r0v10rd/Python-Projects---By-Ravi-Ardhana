'''
1 for rock
-1 for paper
0 for scissor
'''
import random
comp = random.choice([1,-1,0])

you = input("Enter R/P/S: ")

dic= {"R":1,"P":-1,"S":0}
revdic = {1:"Rock",-1:"Paper",0:"Scissor"}

num = dic[you]
print(f"You chose: {revdic[num]}\nComputer chose:{revdic[comp]}")

if(comp==num):
    print("Draw")
elif((comp-num)==-1 or (comp-num)==2):
    print("You Win!")
else:
    print("You Lose!")


'''else:
    if(comp==-1 and num==1): -2
        print("You lose!")
    elif(comp==-1 and num==0): -1
        print("You Win")
    elif(comp==1 and num==-1): 2
        print("You Win")
    elif(comp==1 and num==0): 1
        print("You lose")
    elif(comp==0 and num==-1): 1
        print("You lose")
    elif(comp==0 and num==1): -1
        print("You Win")
    else:
        print("What happened!")'''