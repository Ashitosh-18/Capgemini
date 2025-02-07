def main():
    n = int(input().strip())  # Remove extra spaces from input
    frequency = {}

    for _ in range(n):
        try:
            value = int(input().strip())  # Ensure integer input
            frequency[value] = frequency.get(value, 0) + 1
        except ValueError:
            print("Invalid input! Please enter an integer.")
            return  # Stop execution on error

    # Sort dictionary by key (number values)
    sorted_frequency = sorted(frequency.items())

    # Print results
    for value, count in sorted_frequency:
        print(value, count)

main()
