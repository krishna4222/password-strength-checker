
import string
from getpass import getpass

COMMON_PASSWORDS = {
    "password",
    "password123",
    "12345678",
    "qwerty123",
    "admin123",
    "welcome123"
}


def check_password_strength(password):
    strength = 0
    feedback = []

    # Check whether the password is commonly used
    if password.lower() in COMMON_PASSWORDS:
        print("\nThis is a commonly used password!")
        print("Please choose a different password.")
        return

    checks = [
        (len(password) >= 8,
         "Use at least 8 characters."),

        (any(c.islower() for c in password),
         "Add a lowercase letter."),

        (any(c.isupper() for c in password),
         "Add an uppercase letter."),

        (any(c.isdigit() for c in password),
         "Add a number."),

        (any(c in string.punctuation for c in password),
         "Add a special character.")
    ]

    for passed, message in checks:
        if passed:
            strength += 1
        else:
            feedback.append(message)

    print(f"\nPassword strength score: {strength}/5")

    if len(password) >= 16 and strength == 5:
        print("Very Strong password!")
    elif strength >= 4:
        print("Strong password!")
    elif strength == 3:
        print("Moderate password.")
    else:
        print("Weak password.")

    if feedback:
        print("\nSuggestions:")
        for item in feedback:
            print("-", item)


if __name__ == "__main__":
    password = getpass("Enter your password: ")
    check_password_strength(password)
