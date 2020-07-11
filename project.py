import random
def login_game:
    print('Welcome to the GUESS ME/n')
    print ('give the range for the game')
    global a=int(input())
    global b=int(input())
def generate_no:
    global c=random.randint(a,b)
    return c
def guess_the_no:
    print(f"guess the number between {a} and {b}")
    d=int(input())
def check_limit:
    if c==d:
        print(f" CONGRATULATIONS YOUR GUESS {d} IS CORRECT")
    elif c<d:
        print(f"Your guess {d} is incorrect")
        print(f"Guess someting smaller than {d}") 
    elif c>d:
        print(f"Your guess {d} is incorrect")
        print(f"Guess something greater than {d}")
        
