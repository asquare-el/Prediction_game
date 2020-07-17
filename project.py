import random
def login_game():
    print ('give the range for the game')
    a=int(input())
    b=int(input())
    return a,b 

def generate_no(a,b):
    rand_number=random.randint(a,b)
   
    return rand_number
def guess_the_no(a,b):
    print(f"guess the number between {a} and {b}")
    user_number=int(input())
    return user_number

def check_limit(user_number,rand_number,a,b):
    print(f"\nI have selected a number between {a} and {b}...")
    print("You have 6 chances to guess that number...")
    i = 1
    r = 1
    while i<7:   
        if user_number < rand_number:
            print("\n" + name + ", My number is greater than your guessed number")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif user_number > rand_number:
            print("\n" + name + ", My number is less than your guessed number")
            print("you now have " + str(6-i)+ " chances left" )
            i = i+1
        elif user_number == rand_number:
            print("\nCongratulations "+name+"!! You have guessed the correct number!")
            r = 0
            return
        user_number=int(input("enter the next number"))
    print("you lose")        

def provokation():
    a,b=login_game()
    rand_number=generate_no(a,b)
    user_number=guess_the_no(a,b)
    check_limit(user_number,rand_number,a,b)

name= input("Please enter your name: ")            
print("Welcome to guess the number, "+ name)
provokation()
        
