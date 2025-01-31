def analyze_string(s):
    vowels = "aeiouAEIOU"
    digits = "0123456789"
    vow_count = 0
    cons_count = 0
    digi_count = 0
    spl_char_count = 0
    
    for char in s:
        if char in vowels:
            vow_count += 1
        elif char in digits:
            digi_count += 1
        elif char.isalpha():
            cons_count += 1
        else:
            spl_char_count += 1
    
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string  
 
    print(f"Vowels count: {vow_count}")
    print(f"Consonants count: {cons_count}")
    print(f"Digits count: {digi_count}")
    print(f"Special characters count: {spl_char_count}")
    print(f"Reversed string: {reversed_string}")

def main():
    s = input("Enter a string: ")
    analyze_string(s)

main()