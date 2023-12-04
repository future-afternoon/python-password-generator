import random
import string

def generate_password(length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True):
    characters = ''
    
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_special_chars:
        characters += string.punctuation
    
    if not characters:
        raise ValueError("At least one character set should be selected")
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_multiple_passwords(num_passwords=5, length=12, use_lowercase=True, use_uppercase=True, use_digits=True, use_special_chars=True, max_length=None):
    passwords = []
    for _ in range(num_passwords):
        if max_length:
            current_length = min(length, max_length)
        else:
            current_length = length

        password = generate_password(current_length, use_lowercase, use_uppercase, use_digits, use_special_chars)
        passwords.append(password)
    
    return passwords

# Example usage:
num_passwords = 5
password_length = 16
include_lowercase = True
include_uppercase = True
include_digits = True
include_special_chars = True
max_password_length = 20

passwords = generate_multiple_passwords(num_passwords, password_length, include_lowercase, include_uppercase, include_digits, include_special_chars, max_password_length)

for idx, password in enumerate(passwords, start=1):
    print(f"Password {idx}: {password}")
