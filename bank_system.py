from decimal import Decimal

balance = Decimal("0.00")  # Using Decimal for accuracy

def show_balance():
    print(f"Your balance is ${balance:.2f}")

def deposit():
    global balance
    try:
        amount = Decimal(input("Enter the amount to deposit: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive number.")
            return
        balance += amount
        print(f"${amount:.2f} deposited successfully!")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def withdraw():
    global balance
    try:
        amount = Decimal(input("Enter the amount to withdraw: "))
        if amount > balance:
            print("Insufficient balance.")
            return
        elif amount <= 0:
            print("Amount should be greater than zero.")
            return
        balance -= amount
        print(f"${amount:.2f} withdrawn successfully!")
    except ValueError:
        print("Invalid input. Please enter a numerical value.")

def main():
    is_running = True
    while is_running:
        print("*********************")
        print("\nBanking Program")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        print('**********************')
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            show_balance()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            is_running = False
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
    print("***************************")

    print("Thank you! Have a nice day.")
    print("***************************")
if __name__ == "__main__":
    main()
