import random
import string

chars = string.ascii_lowercase
email = ''.join(random.choice(chars) for i in range(5)) + "@gmail.com"
print('Email: {}'.format(email))

pass_chars = string.digits + string.ascii_lowercase
password = ''.join(random.choice(pass_chars) for i in range(9))
print('Password: {}'.format(password))

