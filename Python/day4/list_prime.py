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
    print(f"Minimum prime number is:{primes[0]}")
    print(f"Maximum prime number is:{primes[-1]}")

main()