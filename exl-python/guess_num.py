import random

system_guess = random.randint(1,5)
flag = True
count = 0

while flag:
    user_guess = int(input("Guess a number between (1 and 5) "))
    if user_guess == system_guess:
        print('Congrats!! You won in ', count)
        flag = False
        break

    elif user_guess < system_guess:
        print("Too low")
        count+=1

    elif user_guess > system_guess:
        print('Too High')
        count+=1

    else: 
        print('Enter a valid number')
        