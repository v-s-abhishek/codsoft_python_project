import random
import string

def generate_password(length):
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    all_characters = lowercase + uppercase + digits + special_characters

    if length < 1:
        return "Password length must be at least 1."

    password = ''.join(random.choice(all_characters) for _ in range(length))

    return password

def main():
    print("Password Generator")
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input! Please enter a numeric value.")
        return

    password = generate_password(length)
    print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
