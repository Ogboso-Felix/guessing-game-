import random
secret_number = random.randint(1,600)
attempts = 0
print("Hello welcome to my number guessing game. \n I am thinking of a number between 1 and 600")
while True:
    guess = int(input("What is the number?"))
    if guess < 1 or guess > 600:
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
