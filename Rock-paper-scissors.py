#rock paper scissor
import random
options = ("rock","paper","scissor")
player = None
running = True
computer = random.choice(options)

while running:
    options = ("rock","paper","scissor")
    player = None
    while player not in options:
        
        player = input("enter a choice(rock,paper,scissor):")
    
    if computer == player:
      
      
      print("tie")
      print(f"player : {player}")
      print(f"computer : {computer}")
    elif player == "rock" and computer == "scissor":
      
      print("you win!")
      print(f"player : {player}")
      print(f"computer : {computer}")
    elif player == "paper" and computer == "rock":
      print("you win!")
      print(f"player : {player}")
      print(f"computer : {computer}")
    elif player == "scissor" and computer == "paper":
      print("you win!")
      print(f"player : {player}")
      print(f"computer : {computer}")
    else:
      print("you lose")    
      print(f"player : {player}")
      print(f"computer : {computer}")
    if input("you want to play again(y/n):")=="n":
        running = False
        
print("Thanks for playing")
    

    
 
 
 
