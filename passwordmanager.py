import random
import string
import os

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_username():
    names = ["John", "Alice", "Robert", "Emily", "Michael", "Emma", "William", "Olivia"]
    name = random.choice(names).lower()
    number = str(random.randint(10, 99))
    return name + number

def generate_complex_password():
    words = ["apple", "banana", "cherry", "date", "elderberry", "fig", "grape", "honeydew"]
    random_word = random.choice(words)

    random_number = str(random.randint(100, 999))

    symbols = "!@#$%^&*"
    random_symbol = random.choice(symbols)

    random_char = random.choice(string.ascii_letters)

    password = random_word + random_number + random_symbol + random_char
    return password

def save_password(website, username, password):
    folder_path = "passwords"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    file_path = os.path.join(folder_path, f"{website}.txt")
    with open(file_path, 'w') as file:
        file.write(f"Website: {website}\n")
        file.write(f"Username: {username}\n")
        file.write(f"Password: {password}\n")

    return file_path

def get_password():
    folder_path = "passwords"
    if not os.path.exists(folder_path) or len(os.listdir(folder_path)) == 0:
        print("No passwords found in the password manager.")
        return

    website = input("Enter the website: ")
    file_path = os.path.join(folder_path, f"{website}.txt")
    if not os.path.exists(file_path):
        username = generate_username()
        password = generate_complex_password()
        file_path = save_password(website, username, password)
        print("Generated username and password:")
        print(f"Username: {username}")
        print(f"Password: {password}")
        print(f"Password saved at: {file_path}")
    else:
        with open(file_path, 'r') as file:
            password_data = file.read()
        print("Password details:")
        print(password_data)
        print(f"Password found at: {file_path}")

def main():
    print("Welcome to the Password Generator and Manager!")

    while True:
        print("\nMENU:")
        print("1. Generate and Save a New Password")
        print("2. Get Password for a Website")
        print("3. Quit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            website = input("Enter the website: ")
            username = generate_username()
            password = generate_complex_password()
            file_path = save_password(website, username, password)
            print("Generated username and password:")
            print(f"Username: {username}")
            print(f"Password: {password}")
            print(f"Password saved at: {file_path}")
        elif choice == '2':
            get_password()
        elif choice == '3':
            print("Thank you for using the Password Generator and Manager!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == '__main__':
    main()
