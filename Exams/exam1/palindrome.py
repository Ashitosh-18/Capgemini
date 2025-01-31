def palindrome(val):
    val = str(val)  
    length = len(val)
    for i in range(length // 2):
        if val[i] != val[length - i - 1]:
            return False
    return True

def main():
    while True:
        user_input = input("Enter a string or number")
        if palindrome(user_input):
            print(f"'{user_input}' is a palindrome.")
        else:
            print(f"'{user_input}' is not a palindrome.")
        

        cont = input("Do you want to continue? (yes/no): ")
        if cont != 'yes':
            break

main()
