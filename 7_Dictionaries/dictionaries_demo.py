# Dictionary is a collection of unordered mutable paired data type.
# key: value

person = {
    "first_name": "John",
    "last_name": "smith",
    "age": 20,
    "gender": "male",
    "birthday": "September 20, 2000"
}

# Accessing this dictionary using Keys
first_name = person["first_name"]
print(first_name)

# Accessing this dictionary using get() method
person_age = person.get("age")
print(person_age)

# Adding new key-value pairs
person["skills"] = "QA"
print(person)

person["skills"] = ["python", "Selenium", "Java", "Maven"]
print(person)

user = {
    "first_name": "John",
    "last_name": "smith",
    "age": 20,
    "skills": ["python", "Selenium", "Java", "Maven"],
    "gender": "male",
    "birthday": "September 20, 2000",
    "address": {
        "Division": "Dhaka",
        "City": "Dhaka",
        "present_address": {
            "house_number": 20,
            "flat": "2a"
        }
    },
    "email": "john@example.com"
}
flat = user["address"]["present_address"]["flat"]
print(flat)

# Check key in Dictionary
print("age" in user)

# Remove key-value
user.pop("birthday")
print("birthday" in user)

# Remove the last item
user.popitem()
print("email" in user)

# Getting all Keys
keys = user.keys()
print(keys)

# Getting all values
values = user.values()
print(values)