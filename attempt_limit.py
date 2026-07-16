
import random
yes_answers = ["yes", "y"]
no_answers = ["no", "n"]
score = 0
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
                attempts_limit = 11
                base_score = 100
                difficulty = "EASY"
                break
            elif choice == 2:
                maximum = 200
                attempts_limit = 8
                base_score = 200
                difficulty = "MEDIUM"
                break
            elif choice == 3:
                maximum = 600
                attempts_limit = 6
                base_score = 300
                difficulty = "HARD"
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
            if guess ==secret_number:
                remaining_attempts = attempts_limit - attempts
                bonus = remaining_attempts * 10
                points_earned = base_score + bonus
                score += points_earned
                print ("=" * 40)
                print("Congratulations!")
                print ("=" * 40)
                print()
                print(f"Difficulty:     {difficulty}")
                print(f"Basescore:      {base_score}")
                print(f"Bonus:          {bonus} ")
                print("-" * 40)
                print(f"Points Earned:  {points_earned}")
                print(f"Current Score:  {score}")
                if attempts == 1:
                    print (f"You guessed the number in {attempts} attempt")
                else:
                    print(f"You guessed the number in {attempts} attempts")
                break
            if attempts >= attempts_limit:
                print ("GAME OVER")
                print(f"The number was {secret_number}")
                print("Better luck next time")
                break
            elif guess > secret_number:
                print("Too high, try again!")
                print(f"You have {attempts_limit - attempts} attempts remaining")
            elif guess < secret_number:
                print("Too low, try again!")
                print(f"You have {attempts_limit - attempts} attempts remaining")
            else:
                print(f"You guessed the number in {attempts} attempts")
                break
        except ValueError:
            print("Please enter a valid number")
            #Ask ↓  Validate  ↓ Invalid? ↓ Tell the user ↓ Ask again
    while True:
            print("Would you like to play the game again \n Y/N")
            response = input("Enter your choice: ")
            response = response.lower()
            if response in yes_answers:
                break
            elif response in no_answers:
                print("=" * 40)
                print(f"Final score:    {score}")
                print()
                print("Thank you for playing!")
                print()
                print("Goodbye!")
                print("=" * 40)
                exit()
            else:
                print("Invalid choice. Please enter Y or N")
                continue