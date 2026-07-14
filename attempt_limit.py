#Where should attemp_limit be set?
#Where should I increase attempts?
#Where should I check if the player has run out of attempt?
#After a valid guess, Python should think:
#Increase attempts....Did the player guess correctly?.....Yes Congratulations! End game.
#No Continue checking...."Has the player reached the attempt limit?" Yes Game Over. 
# Reveal the number. End game. No, Give a hint (Too high/Too low)
#Continue playing. This order ensures that 
# a correct guess on the final allowed attempt is still a win.
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
                attempts_limit = 11
                break
            elif choice == 2:
                maximum = 200
                attempts_limit = 8
                break
            elif choice == 3:
                maximum = 600
                attempts_limit = 6
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
                print("Congratulations!")
                if attempts ==1:
                    print (f"You guessedthe number in {attempts} attempt")
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
            