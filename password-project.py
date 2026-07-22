import re
import secrets
import string
import math

# Check common password List
common_passwords =[
    "password@123",
    "admin@123",
    "welcome@123",
    "password#1",
    "admin#123",
    "qwerty@123",
    "admin#12",
    "welcome#123",
    "qwerty#123"
]

# Calculate password entropy
def calculate_entropy(password):
    charset = 0

    if any(char.islower() for char in password):
        charset += 26

    if any(char.isupper() for char in password):
        charset += 26

    if any(char.isdigit() for char in password):
        charset += 10

    if any(char in string.punctuation for char in password):
        charset += len(string.punctuation)

    if charset == 0:
        return 0
    entropy = len(password) * math.log2(charset)
    return round(entropy, 2)

# Check password strength
def check_password_strength(password):

   
    if password.lower() in common_passwords:
        return "Weak: this is a commonly used password"

    if len(password) < 8:
        return "Weak: password must be at least 8 characters"

    if not any(char.isdigit() for char in password):
        return "Weak: password must contain a digit"

    if not any(char.isupper() for char in password):
        return "Weak: password must contain an upper char"

    if not any(char.islower() for char in password):
        return "Weak: password must contain an lower char"

    if not re.search(r'[!@#$%^*&(){}<>,.?_-]', password):
        return "Medium: password must contain a special character"

    return "Strong: Your password is secured"

# Generete secure password
def generate_password():
    # Try and except to handle the error like input of abc instead of 1,2,3
    try:
        length = int(input("Enter the desired password length: "))
    except ValueError:
        print("Invalid input. Please enter a number")
        return
    
    # Minimum 8 char length validation
    if length <8:
        print("Password length must be at least 8 characters")
        return
    characters = string.ascii_letters + string.digits + string.punctuation
    uppercase = secrets.choice(string.ascii_uppercase)
    lowercase = secrets.choice(string.ascii_lowercase)
    digit = secrets.choice(string.digits)
    special = secrets.choice(string.punctuation)

    remaining_length = length - 4
    remaining = "".join(secrets.choice(characters) for _ in range(remaining_length))

    password = uppercase + lowercase + digit + special + remaining

    password_list = list(password)

    # Shuffle the password
    secrets.SystemRandom().shuffle(password_list)

    password ="".join(password_list)
    
    print("Generated password:", password)
    print("strength of the generated password:",check_password_strength(password))

# Analyse password+security score
def analyze_password(password):
    score = 0
    if len(password) >= 8:
        score += 1
        length_status = "Passed"
    else:
        length_status = "Failed"
    
    if any(char.isupper() for char in password):
        score += 1
        uppercase_status = "Passed"
    else:
        uppercase_status = "Failed"

    if any(char.islower()for char in password):
        score += 1
        lowercase_status = "Passed"
    else:
        lowercase_status = "Failed"
    
    if any(char.isdigit() for char in password):
        score += 1
        digit_status = "Passed"
    else:
        digit_status = "Failed"

    if re.search(r"[!@#$%^&*()_+=\[\]{};:'\\|,.<>\/?-]",password):
        score += 1
        special_status = "Passed"
    else:
        special_status = "Failed"
    
    if password.lower() in common_passwords:
        common_status = "Yes"
    else:
        common_status = "No"

    entropy = calculate_entropy(password)

    if score <= 1:
        strength = "Very weak"
    elif score == 2:
        strength = "Weak"
    elif score == 3:
        strength = "Medium"
    elif score == 4:
        strength = "Strong"
    else:
        strength = "Very Strong"

    print("\n==========PASSWORD SECURITY REPORT==============")
    print("Length Requirement:", length_status)
    print("Uppercase Letter:", uppercase_status)
    print("Lowercase Letter:", lowercase_status)
    print("Digit:", digit_status)
    print("Special Character:", special_status)
    print("Common used Password:", common_status)
    print("Estimated Entropy:", entropy,"bits")
    print("Security Score:", score, "/5")
    print("Password Strength:", strength)
    print("===================================================")

# User input handling area
def password_checker():
        print("Welcome to the password strength checker")

        while True:
            password = input("Enter your password (or type 'exit' to quit): ")

            if password.lower() == 'exit':
                print("thank you for using this tool")
                break
            
            result = check_password_strength(password)
            print(result)


# Main menuPassword security tool
def main_menu():
    while True:
        print("\n=====PASSWORD sECURITY TOOL=====")
        print("1. Check Password Strength")
        print("2. Generate Secure Password")
        print("3. Detailed Password Analysis")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            password_checker()

        elif choice =="2":
            generate_password()

        elif choice == "3":
            password = input("Enter password for detailed analysis: ")
            analyze_password(password)

        elif choice == "4":
            print("Exiting Password Security Tool....")
            break

        else:
            print("Invalid choice. Plese select 1,2,3 or 4.")


#calling the main menu function
if __name__ == "__main__":
    main_menu()