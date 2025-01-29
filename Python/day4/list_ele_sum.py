def main():
    list1 = list(map(int, input("Enter numbers separated by spaces: ").split()))
    sum=0
    for i in list1:
        sum+=i
        
    print (sum)
main()