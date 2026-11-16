
import string
from getpass import getpass

def check_password_strength(password):
    strength = 0
    feedback = []

    checks = [
        (len(password) >= 8, "Password should be at least 8 characters long."),
        (any(c.islower() for c in password), "Add at least one lowercase letter."),
        (any(c.isupper() for c in password), "Add at least one uppercase letter."),
        (any(c.isdigit() for c in password), "Add at least one number."),
        (any(c in string.punctuation for c in password),
         "Add at least one special character.")
    ]

    for passed, message in checks:
        if passed:
            strength += 1
        else:
            feedback.append(message)

    print(f"\nPassword strength score: {strength}/5")

    if strength >= 4:
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
