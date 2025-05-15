# Password Generator

# Step 1: Import proper libraries
import string
import random
import hashlib

# Step 2: Create levels of security
def generate_basic():
    with open("/usr/share/dict/words", "r") as f:
        word_list = f.read().splitlines()
    return random.choice(word_list)

def generate_secure():
    with open("/usr/share/dict/words", "r") as f:
        word_list = f.read().splitlines()

    filtered_words = [word for word in word_list if word.isalpha() and len(word) <= 6]
    base_word = random.choice(filtered_words)

    suffix = ''.join(random.choices(string.digits + "!@$^&*", k=3))

    return base_word + suffix

def generate_confidential(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_hashed_password():
    length = 12  # or whatever fixed length you prefer
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    hashed = hashlib.sha256(password.encode()).hexdigest()
    return hashed

# Step 3: Create user input
def main():
    choice = input(
        "\nChoose level of security:\n"
        "- Basic = simple word\n"
        "- Secure = word+numbers+characters\n"
        "- Confidential = completely randomized characters\n"
        "- Hashed = SHA-256 Encryption *fixed length*\n"
        "Enter your choice: "
    ).strip().lower()

    if choice == "basic":
        password = generate_basic()
        print(f"Generated Password: {password}")
    elif choice == "secure":
        password = generate_secure()
        print(f"Generated Password: {password}")
    elif choice == "confidential":
        length = int(input("Enter password length: "))
        password = generate_confidential(length)
        print(f"Generated Password: {password}")
    elif choice == "hashed":
        hashed = generate_hashed_password()
        print(f"SHA-256 Hashed Password: {hashed}")
    else:
        print("Invalid choice. Please enter: basic, secure, confidential, or hashed.")

if __name__ == "__main__":
    main()
# Step 4: Test the program

