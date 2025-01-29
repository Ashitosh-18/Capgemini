def prime_notprime(num):
    if num==1 or 0:
        return("not prime")
    if num%2==0:
        return False
    else:
        k=int(num**0.5)
        for i in range(3,k+1):
            if num%i==0:
                return False
        return True    
        
def main():
    num=int(input("enter number:"))
    p=prime_notprime(num)
    if p==True:
        print("prime number")
        
    else:
        print(" not a prime number")
        
main()
    
    