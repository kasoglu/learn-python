import random

guessTaken = 0

number = random.randint(1,100)

print("Welcome to Guess Number Game")
print("What's yourn name?")
name = input()

print(f"Well, {name} Can you tell me number (1,20)")

while guessTaken < 6:
    print("Take a guess!")
    guess = input()
    guess = int(guess)

    guessTaken += 1

    if guess < number:
        print("Your guess lower than the number.")
    
    if guess > number:
        print("Your guess higher than the number.")

    if guess == number:
        break

if guess == number:
    guessTaken = str(guessTaken)
    print(f"Congrutulations! {name}. You guessed the number {guessTaken} times. ")
    print(f"The number is I guessed {number}.")

if guess != number:
    number = str(guess)
    print(f"Nope! {name} The number I was thinking of is {number}.")

