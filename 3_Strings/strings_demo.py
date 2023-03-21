# String Concatenation
first_name = "Mr."
last_name = "smith"

full_name = first_name + " " + last_name
# print(full_name)

# Escape Sequence
"""
\n : new line
\t : Tab means 8 space
\\ : Back slash
\' : Single quote
\" : Double quote
"""

print("hello \n" + full_name)
print("hello \t" + full_name)

print("Hello 'dhaka'")

# String formatting : old
"""
%s : String
%d : Number/Integer
%f : Float
"""
age = 20
formatting_string = 'I am %s %d' % (first_name, age)
print(formatting_string)

# String formatting : new
tax = 20.5
new_formatting_string = 'I am {} {}'.format(first_name, tax)
print(new_formatting_string)

# String slicing
language = 'Python3'
first_three = language[:3]  # starts at zero index and up tp 3 but not include 3
print(first_three)
last_three = language[3:6]
print(last_three)
# last = language[3:len(language)]
last = language[3:]
print(last)

# Reverse
message = "Hello, world!"
print(message[::-1])

# String Methods
name = 'brown kevin'
print(name.capitalize())  # Brown kevin
print(name.title())  # Brown Kevin
print(name.count('n'))  # returns occurrence of substring
print(name.find('n'))  # returns the index of first occurrence of substring

challenge = "LearningPython123"
print(challenge.isalnum())  # True

challenge2 = "LearningPython"
print(challenge2.isalpha())  # True

# Remove Space
success_message = "Congratulations Hello World"
new_success_message = success_message.replace(" ", "")  # remove spaces
print(new_success_message)

length = len(success_message)
print(length)
