import random
while True:
    print("=" * 40)
    print("WELCOME TO MY NUMBER GUESSING GAME")
    print("=" * 40)
    print("\nChoose a Difficulty")
    print("1. EASY")
    print("2. MEDIUM")
    print("3. HARD")
    while True:
        try:
            choice = int(input("Enter your choice:"))
            if choice == 1:
                maximum = 50
                break
            elif choice == 2:
                maximum = 200
                break
            elif choice == 3:
                maximum = 600
                break
            else:
                print("Invalid choice. Choose 1, 2, or 3.")
        except ValueError:
            print("Please enter a valid number")
    secret_number = random.randint(1, maximum)
    attempts = 0
    print(f"Great! I am thinking of a number between 1 and {maximum}")
    while True:
        try:
            guess = int(input("What is the number?"))
            if guess < 1 or guess > maximum:
                print("Follow the rule of the game!")
                continue
            attempts +=1
            if guess > secret_number:
                print("too high")
            elif guess < secret_number:
                print("too low")
            else:
                print(f"correct! You got it in {attempts} attempts")
                break
        except ValueError:
            print("Please enter a valid number")
            