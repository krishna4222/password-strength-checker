import string

def check_password_strength(password):
    strength = 0
    feedback = []

    if len(password) >= 8:
        strength += 1
    else:
        feedback.append("Password should be at least 8 characters long.")

    if any(char.islower() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one lowercase letter.")

    if any(char.isupper() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one uppercase letter.")

    if any(char.isdigit() for char in password):
        strength += 1
    else:
        feedback.append("Add at least one number.")

    if any(char in string.punctuation for char in password):
        strength += 1
    else:
        feedback.append("Add at least one special character (!, @, #, etc.)")

    if strength >= 4:
        print("✅ Strong password!")
    else:
        print("⚠️ Weak password:")
        for item in feedback:
            print("-", item)

# Example usage:
password = input("Enter your password: ")
check_password_strength(password)
