import random

number=random.randint(1,9)
#print(number)
chances=0

while chances < 5:
   # print(chances)
    guess=int(input("What is your Guess? Enter a number from 1-9."))
   # print(guess)
    # print(number)
    
    if guess == number:
        print("You are a winner.")
        break
    elif guess > number:
        print("You guessed to high! Guess lower!")
    elif guess < number:
        print("You guessed to low! Guess higher!")
    chances+=1
    if(chances == 5):
        print("You loose. The number is",number)


    