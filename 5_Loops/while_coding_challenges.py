"""
Challenge: Write a program that ask user to enter a number between 1 and 10
If the user entered a number outside the range,
ask again until the user entered a number.
"""
"""
num = int(input('Enter a number: '))

while num < 1 or num > 10:
    num = int(input('Enter a number between 1 and 10 : '))

print("Thanks for entering between 1 and 10")
"""

"""
Challenge: Write a program that ask user to enter password
If the user entered invalid password,
ask again until the user entered a valid password.
"""

password = "123456"
user_password = input("Enter your password: ")

while password != user_password:
    print("Login failed!!")
    user_password = input("Enter your password again: ")

print("Login Successfully")
