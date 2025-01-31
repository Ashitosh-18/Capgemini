import random

def main():
    secret_num = random.randint(1, 100)
    print("Guess the number (between 1 and 100):")

    while True:
        guess = int(input("Enter your guess: "))
        if guess < secret_num:
            print("Too Low!")
        elif guess > secret_num:
            print("Too High!")
        else:
            print("Congratulations! You guessed it!")
            break

main()
