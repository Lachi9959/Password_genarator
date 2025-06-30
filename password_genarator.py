import random
import string

def generate_password(length=12, use_upper=True, use_lower=True, use_digits=True, use_symbols=True):
    characters = ''
    if use_upper:
        characters += string.ascii_uppercase
    if use_lower:
        characters += string.ascii_lowercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        return "Error: No character sets selected."

    # Ensure at least one character from each selected type
    password = []
    if use_upper:
        password.append(random.choice(string.ascii_uppercase))
    if use_lower:
        password.append(random.choice(string.ascii_lowercase))
    if use_digits:
        password.append(random.choice(string.digits))
    if use_symbols:
        password.append(random.choice(string.punctuation))

    while len(password) < length:
        password.append(random.choice(characters))

    random.shuffle(password)
    return ''.join(password)

# === Run the password generator ===
if __name__ == "__main__":
    print("🔐 Password Generator")
    try:
        length = int(input("Enter desired password length (e.g. 12): "))
        password = generate_password(length)
        print("Generated Password:", password)
    except ValueError:
        print("Please enter a valid number.")
