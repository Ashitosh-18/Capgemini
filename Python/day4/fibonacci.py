def fibo(num):
    if num <= 0:
        return []
    elif num == 1:
        return [0]
    elif num == 2:
        return [0, 1]

    res = [0, 1]  # Start with the first two Fibonacci numbers
    for _ in range(2, num):
        res.append(res[-1] + res[-2])  # Add the last two numbers in the list
    return res

def main():
    num = int(input("Enter the number of Fibonacci terms: "))
    if num < 0:
        print("Please enter a non-negative number.")
    else:
        res = fibo(num)
        print(f"Fibonacci sequence with {num} terms: {res}")

main()
