
# 🔐 Password Strength Checker

A simple Python-based application that evaluates password strength using five predefined security rules and provides feedback to help users create stronger passwords.

## 📌 Project Overview

This project checks whether a password meets basic security requirements by examining its length, character types and use of special characters.

The program calculates a strength score and displays whether the password is strong or weak.

## ✨ Features

- Checks minimum password length (8 characters).
- Detects lowercase letters.
- Detects uppercase letters.
- Checks for numeric digits.
- Identifies special characters.
- Calculates a password strength score.
- Provides feedback when password requirements are not met.

## 🛠️ Technologies Used

- Python 3
- string module
- Built-in Python functions

## ⚙️ How It Works

The program evaluates a password against five conditions:

1. At least 8 characters.
2. At least one lowercase letter.
3. At least one uppercase letter.
4. At least one number.
5. At least one special character.

Each satisfied condition adds one point to the score.

- 4–5 points: Strong password.
- 0–3 points: Weak password.

## 🚀 How to Run

1. Clone this repository:

   ```bash
   git clone https://github.com/krishna4222/password-strength-checker.git
   ```

2. Open the project folder:

   ```bash
   cd password-strength-checker
   ```

3. Run the Python program:

   ```bash
   python password_checker.py
   ```

4. Enter a password when prompted.

## 💻 Example Output

**Example: Strong password**

```text
Enter your password: Secure@123
Strong password!
```

**Example: Weak password**

```text
Enter your password: hello
Weak password:
- Password should be at least 8 characters long.
- Add at least one uppercase letter.
- Add at least one number.
- Add at least one special character (!, @, #, etc.)
```

## 🎯 Learning Outcomes

- Python conditional statements.
- Functions and loops.
- String manipulation.
- Password validation.
- Basic cybersecurity concepts.

## ⚠️ Limitations

This is a basic educational, rule-based password checker. It does not assess password reuse, dictionary attacks, breached passwords or resistance to advanced guessing techniques.

It should not be treated as a complete password-security assessment tool.

## 👨‍💻 Author

**Krishna Rungta**

MSc Cyber Security Student – Aston University, UK

[GitHub](https://github.com/krishna4222)
[LinkedIn](https://www.linkedin.com/in/krishna4222)
