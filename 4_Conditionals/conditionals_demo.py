a = 3

if a > 4:
    print("Hello")
else:
    print("world")

if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is a zero')

if a > 0:
    if a % 2 == 0:
        print('A is a positive number and even')
    elif a % 2 == 1:
        print('A is a negative number and')
    else:
        print('A is a positive number and odd')
elif a < 1:
    print('A is a negative number')
elif a <= 0:
    print("A is a negative number and below zero")
else:
    print('A is a zero')