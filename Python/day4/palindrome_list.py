def find_palin(lst1):
    lst2=lst1[::-1]
    if lst1==lst2:
        return "it is a plindrome"
    else:
        return "it is not a palindrome"
    
    
def main():
    lst1=list(input("enter the text:"))
    res=find_palin(lst1)
    print(res)
main()
    
