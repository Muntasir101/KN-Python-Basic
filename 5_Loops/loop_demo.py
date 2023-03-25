"""
1. for
2. while

While: When the number of iteration is not fixed then we use while loop.
"""

"""
while True:
     code executed
     
while False:
    Jump to next statement
"""

count = 1
while count < 5:
    print(count)
    count += 1
    break
else:
    print(count)

for i in range(5):
    print("hello world")
