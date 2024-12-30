import random
n= random.randint(1,100)
print("WELCOME TO GUESS THE NUMBER!")
print("Let me select a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")
a=-1
guesses=[]
try:
    while(a!=n):
            a = int(input("Guess the number:"))
            if(a>100 or a<1):
                print("Your guess is out of range.\nPlease guess a number between 1-100")
                continue
            guesses.append(a)
            d = abs(n-a)
            if len(guesses)==1:
                if(d<=10):
                    print("Getting Warm!",n)
                else:
                    print("Getting Cold!",n)
            else:
                if(d<abs(n-guesses[-2])):
                    print("You're getting WARMER!")
                else:    
                    print("You're getting COLDER!")
    print(f"You have guessed the number({n}) correctly in {len(guesses)} attempts.")
    with( open("Scorecard.txt","r") as f1,
        open("Scorecard.txt","a") as f2):
            i = len(f1.readlines())
            f2.write(f"Player{i+1}: {len(guesses)}\n")
except KeyboardInterrupt as k:
    print("\nSee you next time!")
except ValueError as e:
    print ("Enter a valid number!!")
    
    
