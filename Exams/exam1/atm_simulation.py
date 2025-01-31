def check_balance(balance):
    print(f"\nYour balance is: {balance}")

def deposit(balance):
    amount = int(input("\nEnter the amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"{amount:} deposited successfully.")
    else:
        print("Enter a valid amount.")
    return balance

def withdraw(balance):
    amount = int(input("\nEnter the amount to withdraw: "))
    if amount > balance:
        print("Insufficient balance.")
    elif amount > 0:
        balance -= amount
        print(f"{amount} withdrawn successfully.")
    else:
        print("Invalid amount. Please enter a positive value.")
    return balance

def main():
    balance = 1000.0 
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            check_balance(balance)
        elif choice == '2':
            balance = deposit(balance)
        elif choice == '3':
            balance = withdraw(balance)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

main()

