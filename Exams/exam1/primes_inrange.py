def get_input():
    n1=int(input("Enter n1:"))
    n2=int(input("Enter n2:"))
    
    return n1,n2

def prime(num):
    if num<2:
        return False
    if num==2:
        return True
    if num%2==0:
        return False
    
    k=int(num**0.5)
    
    for i in range(3,k+1):
        if num%i==0:
            return False
    return True

def range_num(n1,n2):
    primes=[]
    for num in range(n1,n2+1):
        if prime(num):
            primes.append(num)
    return primes

def main():
    n1,n2=get_input()
    res=range_num(n1,n2)
    print(f"prime numbers between {n1} and {n2} are: {res}")
    
main()
        