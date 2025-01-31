def fact(n):
    res=1
    if n>0:     
        for i in range(1,n+1):
            res*=i
            
        return res
    else:
        print("Enter a positive number only")

def main():
    n=int(input("enter n value:"))
    val=fact(n)
    print(val)
    
main()