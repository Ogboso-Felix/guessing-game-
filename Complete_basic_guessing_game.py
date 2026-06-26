import random
print("=" * 40)
print("WELCOME TO MY NUMBER GUESSING GAME")
print("=" * 40)
print("\nChoose a Difficulty")
print("1. EASY")
print("2. MEDIUM")
print("3. HARD")
choice = int(input("Enter your choice:"))
if choice == 1:
    maximum = 50
elif choice == 2:
    maximum = 200
elif choice == 3:
    maximum = 600
else:
    print("Invalid choice. Defaulting to Hard difficulty.")
    maximum = 600
secret_number = random.randint(1, maximum)
attempts = 0
print(f"Great! I am thinking of a number between 1 and {maximum}")
while True:
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
