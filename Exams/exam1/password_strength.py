def check_password_strength(password):
    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

   
    for char in password:
        if char.isupper():
            has_upper = True
        elif char.islower():
            has_lower = True
        elif char.isdigit():
            has_digit = True
        elif not char.isalnum():
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        return "Strong password"
    else:
        return "Weak password"

def main():
    password = input("Enter a password: ")
    result = check_password_strength(password)
    print(result)

main()