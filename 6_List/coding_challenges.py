# print the sum of list
number = [12, 33, 45, 55]
total = 0
for i in number:
    total += i
print(total)

# create a new list with even numbers only
even_list = []
for i in number:
    if i % 2 == 0:
        even_list.append(i)
print(even_list)

# print each string in uppercase and crate a new list
skills = ["python", "selenium", "Java", "Maven"]
new_skills = []
for word in skills:
    new_skills.append(word.upper())
print(new_skills)

# print the largest number
numbers = [1, 23, 43, 56, 76, 88, 90, 100]
max_number = numbers[0]
for num in numbers:
    if num > max_number:
        max_number = num
print(max_number)

# create list by user given single data
data = input("Enter your data: ")
numbers.append(data)
print(numbers)

# create list by user given multiple data
user_data = []
while True:
    user_input = input("Enter your data or type 'exit' to stop: ")
    if user_input == "exit":
        break
    else:
        user_data.append(user_input)

print(user_data)
