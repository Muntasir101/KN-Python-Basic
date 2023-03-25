"""
# 1 to 10 only even number
for i in range(10):
    if i % 2 == 0:
        print(i)

for iteration in range(0, 10, 2):
    print(iteration)
"""

message = 'Hello, world Dhaka'
vowels = 'aeiou'
count = 0

for char in message:
    if char in vowels:
        count += 1
print(count)

