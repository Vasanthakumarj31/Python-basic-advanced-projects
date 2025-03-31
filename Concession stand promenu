#concession stand promenu 
menu = {
    
        "Idli": 30,
        "Dosa": 40,
        "Pongal": 50,
        "Vada": 20,
        "Sambar Rice": 70,
        "Curd Rice": 60,
        "Lemon Rice": 65,
        "Meals": 120,
        "Bajji": 25,
        "Sundal": 30,
        "Murukku": 20,
        "Paruppu Vada": 25
    }

total = 0
print("------------------menu-----------------")

for keys,values in menu.items():
   print(f"{keys :15} : {values}")
print("--------------------------------------------")

cart = []
while True:
    food = input("enter the food(q to exit):").title()
    if food.lower() == "q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("the food is not found")
print("------------your order----------------")

for food in cart:
    total += menu.get(food)
    print(food,end = " ")
   
print()

print(f"the total cost of food is {total}")

 
