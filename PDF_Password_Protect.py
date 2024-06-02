import pikepdf, os, secrets, string, pyperclip
from pathlib import Path

def get_location():
    """
    Prompts the user to enter a file path and validates it.
    Returns a tuple containing the file path and its parent directory.
    """
    while True:
        try:
            filepath = Path(input(r"Enter the filepath: ").strip('"'))
            if filepath.is_file():
                return filepath, filepath.parent
            else:
                print("Invalid file path. Please try again.")
        except ValueError:
            print("Invalid file path format. Please try again.")

def get_name(filepath):
    """
    Extracts the filename without the extension from the given file path.
    Returns the filename as a string.
    """
    return filepath.stem

def get_password(user_type):
    """
    Prompts the user to enter a password for the specified user type.
    Returns the entered password as a string.
    """
    while True:
        password = input(f"\nEnter the password for the file {user_type}: ")
        if password:
            return password
        else:
            print("Password cannot be empty. Please try again.")

def generate_password(length=20):
    """
    Generates a secure random password with the specified length.
    Copies the generated password to the clipboard.
    Prints the generated password to the console.
    Returns the generated password as a string.
    """
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for _ in range(length))
    pyperclip.copy(password)
    print(f"\nUser password: {password}\n")
    return password

def main():
    """
    Main function to handle the password protection process.
    Prompts the user for a file path and owner password.
    Generates a secure user password.
    Password-protects the PDF file with the provided owner password and generated user password.
    """
    os.system("cls")  # Clear the console screen (only works on Windows)

    # Get the file path and location from the user
    filepath, location = get_location()

    # Open the PDF file
    pdf = pikepdf.Pdf.open(filepath)

    # Get the filename without the extension
    name = get_name(filepath)

    # Create a new filename with the '(SECURED)' suffix
    encrypted_name = f"{name} (SECURED).pdf"
    encrypted_path = location / encrypted_name

    # Password-protect the PDF file with the owner password and generated user password
    pdf.save(encrypted_path, encryption=pikepdf.Encryption(
        owner=get_password("owner"),
        user=generate_password(),
        R=6  # Encryption level (6 is the recommended default)
    ))

    # Close the PDF file
    pdf.close()

if __name__ == "__main__":
    main()
