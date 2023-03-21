import random  # Build-in function

number = random.randint(1, 5)

guess = int(input("Guess a Number: "))

if guess == number:
    print("Congratulations !! You Win!")
else:
    print("Sorry !! You loose. actual number is ", number)
