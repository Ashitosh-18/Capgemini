def main():
    while True:
        bill = int(input("Enter total bill amount: "))
        people = int(input("Enter number of people: "))
        tip = int(input("Enter tip percentage: "))

        if bill < 0 or people <= 0 or tip < 0:
            print("Please enter positive values.")
            continue

        total = bill + (bill * tip / 100)
        per_person = total / people
        print(f"Each person should pay: {per_person}")

        cont = input("Do you want to calculate another bill? (yes/no): ")
        if cont != 'yes':
            break

main()
