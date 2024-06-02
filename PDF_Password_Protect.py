import pikepdf, os, secrets, string, pyperclip
from pathlib import Path

def get_location():
    """Gets the file path and location from user input."""
    while True:
        try:
            filepath = Path(input(r"Enter the filepath: ").strip('"'))
            if filepath.is_file():  # Check if it's a valid file
                return filepath, filepath.parent
            else:
                print("Invalid file path. Please try again.")
        except ValueError:
            print("Invalid file path format. Please try again.")

def get_name(filepath):
    """Extracts the filename without extension."""
    return filepath.stem

def get_password(user_type):
    """Prompts for and returns a password."""
    while True:
        password = input(f"\nEnter the password for the file {user_type}: ")
        if password:  # Check if password is not empty
            return password
        else:
            print("Password cannot be empty. Please try again.")

def generate_password(length=20):
    """Generates a secure random password with the specified length."""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    print(f"\nUser password: {password}\n")
    return password

def main():
    """Main function to handle password protection."""
    os.system("cls")  # Optional: Clear console

    filepath, location = get_location()
    pdf = pikepdf.Pdf.open(filepath)
    name = get_name(filepath)

    encrypted_name = f"{name} (SECURED).pdf"
    encrypted_path = location / encrypted_name

    pdf.save(encrypted_path, encryption=pikepdf.Encryption(
        owner=get_password("owner"),
        user=generate_password(),
        R=6  # Encryption level (6 is the recommended default)
    ))
    pdf.close()

if __name__ == "__main__":
    main()
