import random
import string

length = 8

upper = random.choice(string.ascii_uppercase)
lower = random.choice(string.ascii_lowercase)
digit = random.choice(string.digits)
special = random.choice(string.punctuation)

password = upper + lower + digit + special

all_characters = string.ascii_letters + string.digits + string.punctuation

for i in range(length - 4):
    password += random.choice(all_characters)

password = ' '.join(random.sample(password, len(password)))
print("Generated Password: ", password)