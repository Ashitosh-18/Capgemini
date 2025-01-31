def cel_to_far(cel):
    return (cel*9/5)+32

def far_to_cel(far):
    return (far-32)*5/9

def cel_to_kel(cel):
    return (cel+273)

def kel_to_cel(kel):
    return (kel-273)

def far_to_kel(far):
    return (far-32)*5/9+273

def kel_to_far(kel):
    return (kel-273)*9/5+32

def main():
    while True:
        print("Choose the temperature conversion:")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. Celsius to Kelvin")
        print("4. Kelvin to Celsius")
        print("5. Fahrenheit to Kelvin")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")

        choice = input("select one option: ")

        if choice == '1':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C = {cel_to_far(celsius)}°F")
        elif choice == '2':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F = {far_to_cel(fahrenheit)}°C")
        elif choice == '3':
            celsius = float(input("Enter temperature in Celsius: "))
            print(f"{celsius}°C = {cel_to_kel(celsius)}K")
        elif choice == '4':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin}K = {kel_to_cel(kelvin)}°C")
        elif choice == '5':
            fahrenheit = float(input("Enter temperature in Fahrenheit: "))
            print(f"{fahrenheit}°F = {far_to_kel(fahrenheit)}K")
        elif choice == '6':
            kelvin = float(input("Enter temperature in Kelvin: "))
            print(f"{kelvin}K = {kel_to_far(kelvin)}°F")
        elif choice == '7':
            break
        else:
            print("Invalid choice, please try again.")

main()

