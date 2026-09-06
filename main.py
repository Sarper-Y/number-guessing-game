import random
number = random.randint(1, 100)
attempts = 0
guess = 0
max_attempts = 10
print("Guess the number")
print("You Have", max_attempts, "attemps")
while guess != number and attempts < max_attempts:
    guess = int(input("your guess: "))
    if guess < 1 or guess > 100:
        print("Please write between 1 and 100.")
        continue
    attempts = attempts + 1
    if guess == number:
        print("Correct")
    elif guess > number:
        print("Too high")
    else:
        print("Too low")
    print("Remaining attemps :", max_attempts - attempts)
if guess != number:
    print("Attemps are over coerrect number was", number,)
print("Total attemps:", attempts)