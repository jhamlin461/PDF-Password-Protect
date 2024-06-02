# PDF Password Protector
This Python script provides a simple way to add password protection to PDF files using the pikepdf library. It encrypts the PDF with a user-defined password for the owner (you) and a secure, randomly generated password for the user (recipient).

# Features
**Strong Encryption:** Utilizes AES encryption with 256-bit keys.

**Owner and User Passwords:** Sets separate passwords for the owner (you) and the user who will open the document.

**Secure Password Generation:** The user password is generated randomly and copied to your clipboard for convenience.

**Customizable:** You can modify the password length and other parameters.

**Clear Instructions:** Prompts guide you through the process.

# Installation
Ensure you have Python3 installed. Install required libraries using pip:

**pip install pikepdf pyperclip** 

# Usage
Run the script.

Enter the file path to the PDF you want to protect.

Provide a password for the "owner" (yourself).

The script will generate a strong password for the "user," copy it to your clipboard, and print it to the console.

A new file named [original_filename] (SECURED).pdf will be created in the same directory as the original PDF.

# Code Overview
**get_location():** Obtains the file path from the user.

**get_name():** Extracts the filename without the extension.

**get_password():** Prompts for a password and validates it's not empty.

**generate_password():** Creates a secure random password for the user.

**main():** Orchestrates the entire password protection process.

# Security Considerations
**Password Storage:** The script does not store passwords in any way. It's your responsibility to remember the owner password and securely manage the generated user password.

**Encryption Level:** The script uses the recommended default encryption level (R=6).

# Contributing
Feel free to fork this repository and submit pull requests if you'd like to enhance this script or contribute new features!

# License
This project is open-source and available under the MIT License.

Let me know if you have any specific changes you'd like to make to the README!
