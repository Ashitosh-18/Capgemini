# def find_palin(lst):
#     k=lst[::-1]
#     if lst==k:
#         return "it is a plindrome"
#     else:
#         return "it is not a palindrome"
    
def remove_extra_spaces(sentence):
    result = []
    in_space = False
    
    for char in sentence:
        if char == " ":
            # Only append the space if it is not a consecutive one
            if not in_space:
                result.append(char)
                in_space = True
        else:
            result.append(char)
            in_space = False
    
    # Return the final result, which will already be without leading/trailing spaces
    if result and result[0] == " ":
        result.pop(0)  # Remove leading space if any
    if result and result[-1] == " ":
        result.pop()  # Remove trailing space if any
    
    return ''.join(result)

def main():
    sentence = input("Enter a sentence: ")
    result = remove_extra_spaces(sentence)
    print("Sentence without extra spaces:", result)

main()
