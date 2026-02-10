import random
import numpy as np
print("Welcome to the Number Guessing Game!😉")
response="yes"
while response.lower()=="yes":
    start=int(input("Enter the start of the range: "))
    end=int(input("Enter the end of the range: "))
    num=random.randint(start,end)
    attempts=0
    try: 
        guess=int(input(f"guess the number between {start} and {end}: "))
        attempts+=1
    except ValueError:
        print("Your input is invalid!'❌")
    while True:
        if guess==num:
             print("✅ Your guess is correct!", num)
             break
        elif guess<num:
            
            guess=int(input(" Your guess is low, think higher .👆: "))
            attempts+=1
        else:
            guess=int(input(" Your guess is high, think lower 👇: "))
            attempts+=1
    mean=np.mean([start,end])
    if attempts==1:
        print(f"🎉 Amazing! You guessed it in just {attempts} attempts!")

    elif attempts<int(mean):
        print(f"🎉 Great job! You guessed it in {attempts} attempts!")
    else:
        print(f"👍 You guessed it in {attempts} attempts. Better luck next time!")
    response=input("Do you want to play again? (yes/no): ")
    if response.lower()=="no":
        print("Thank you for playing! Goodbye!🖐")
        break