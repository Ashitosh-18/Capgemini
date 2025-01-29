# def get_input():
#     n1=int(input("enter n1:"))
#     n2=int(input("enter n2:"))
    
#     return(n1,n2)
    
# def prime_notprime(n1,n2):
#     if n1==1 or 0:
#         return("not a prime number")
#     if n1%2==0:
#         return False
#     else:
#         k=int(n1**0.5)
        
#         for j in range(n1,n2+1):
#             for i in range(3,k+1):
#                 if j%i==0:
#                     return False
#             return j  
#         return True  
        
# def main():
#     n1,n2=get_input()
#     p=prime_notprime(n1,n2)
    
#     print(p)
    
    
#     # if p==True:
#     #     print("prime number")
        
#     # else:
#     #     print(" not a prime number")
        
# main()
    
    
    
def get_input():
    n1 = int(input("Enter n1: "))
    n2 = int(input("Enter n2: "))
    return n1, n2

def is_prime(num):
    if num < 2:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True

def prime_numbers_in_range(n1, n2):
    primes = []
    for num in range(n1, n2 + 1):
        if is_prime(num):
            primes.append(num)
    return primes

def main():
    n1, n2 = get_input()
    primes = prime_numbers_in_range(n1, n2)
    print(f"Prime numbers between {n1} and {n2}: {primes}")

main()

    