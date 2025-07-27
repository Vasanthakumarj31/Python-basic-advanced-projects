#python number guessing game
import random

lowest_num = 1
highest_num = 100
answer = random.randint(lowest_num,highest_num)
guesses = 0
is_running= True

print("python number guessing game")
print(f"Select the number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("enter the number:")
    if guess.isdigit():
        guess = int(guess)
        guesses +=1
        if  guess<lowest_num or guess>highest_num:
            print("out of range")
            print(f"please Select the number between {lowest_num} and {highest_num}")
        elif guess<answer:
            print("too low!try again")
        elif guess>answer:
            print("too high!try again")
        else:
            print(f"CORRECT!The answer is {answer}")
            print(f"the total guesses are {guesses}")
            is_running=False
    else:
        print("invalid guesses")
        print(f"please Select the number between {lowest_num} and {highest_num}")
