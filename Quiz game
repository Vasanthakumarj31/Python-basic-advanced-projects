questions = (
    "What is your name?",  
    "How old are you?",  
    "Where do you live?",  
    "What is your favorite color?",  
    "What do you do for a living?"  
)
options = (
    ("A) John", "B) Alice", "C) Your Name", "D) Michael"),
    ("A) 10", "B) 20", "C) 30", "D) 40"),
    ("A) USA", "B) UK", "C) Canada", "D) Your City"),
    ("A) Red", "B) Blue", "C) Green", "D) Yellow"),
    ("A) Student", "B) Engineer", "C) Doctor", "D) Your Profession")
)
answers=("C","B","D","A","A")
guesses=[]
score=0
questionn=0

for  question in questions:
    print("---------------------------------------------------------")
    print(question)
    for option in options[questionn]:
        print(option)
        
    guess=input("enter (A,B,C,D)").upper()
    guesses.append(guess)
    if guess==answers[questionn]:
         score += 1
         
         print("correct")
    else:
        print("incorrect")
        print(f"{answers[questionn]} is the correct answer")
        
    questionn += 1
    
print("-------------------------------------------------")
print("                      result                           ")
print("-------------------------------------------------")
for  answer in answers:
       print(answer,end=" ")
print()
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score/len(questions)*100)
print(f"score percentage: {score}%")
    
