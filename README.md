# 🔐 Password Strength Checker

A simple Python-based cybersecurity project that evaluates password strength using predefined security rules and provides suggestions to improve weak passwords.

## 👨‍💻 About the Project

This project was developed to understand basic password security concepts and Python programming.

The Password Strength Checker analyses a password against five security conditions and calculates a score out of 5. Based on the score, it classifies the password as **Strong**, **Moderate**, or **Weak**.

## ✨ Features

- Checks whether the password contains at least 8 characters.
- Checks for lowercase letters.
- Checks for uppercase letters.
- Checks for numeric digits.
- Checks for special characters.
- Calculates a password strength score out of 5.
- Provides suggestions when password requirements are missing.
- Uses hidden password input through Python's `getpass` module.

## 🛠️ Technologies Used

- **Programming Language:** Python
- **Editor:** Visual Studio Code
- **Libraries:** `string`, `getpass`
- **Version Control:** Git and GitHub

## 📋 Password Evaluation Rules

| Security Requirement | Description | Score |
|---|---|---:|
| Minimum Length | At least 8 characters | 1 |
| Lowercase Letter | At least one lowercase letter | 1 |
| Uppercase Letter | At least one uppercase letter | 1 |
| Number | At least one digit | 1 |
| Special Character | At least one special character | 1 |
| **Total** | | **5** |

### Password Classification

- **4–5 points:** Strong Password
- **3 points:** Moderate Password
- **0–2 points:** Weak Password

## 🚀 How to Run the Project

### Step 1: Clone the Repository

```bash
git clone https://github.com/krishna4222/password-strength-checker.git
```

### Step 2: Open the Project Folder

```bash
cd password-strength-checker
```

### Step 3: Run the Python Program

```bash
py password_checker.py
```

You can also use:

```bash
python password_checker.py
```

If the `python` command is not recognised on Windows, try `py`.

### Step 4: Enter a Test Password

The program will ask you to enter a password. Your input is hidden while typing.

## 🧪 Testing and Results

The program was tested with different password inputs.

### Test 1: Strong Password

**Expected behaviour:** The program should identify a password meeting all five conditions.

```text
Password strength score: 5/5
Strong password!
```

**Status:** Passed

### Test 2: Weak Password

**Expected behaviour:** The program should identify missing password requirements and display suggestions.

```text
Password strength score: 1/5
Weak password.

Suggestions:
- Password should be at least 8 characters long.
- Add at least one uppercase letter.
- Add at least one number.
- Add at least one special character.
```

**Status:** Passed

### Test 3: Moderate Password

**Expected behaviour:** A password meeting exactly three conditions should receive a score of 3/5 and be classified as Moderate.

**Status:** Pending testing

## 🎯 Learning Outcomes

Through this project, I practised:

- Python functions and conditional statements.
- Lists and loops.
- String manipulation.
- Password validation techniques.
- Using Python's built-in modules.
- Basic cybersecurity and password security concepts.
- Testing and documenting a Python project.
- Using GitHub for project version control.

## ⚠️ Limitations

This is a basic educational, rule-based password checker.

It does not evaluate:

- Password reuse.
- Dictionary-based password attacks.
- Previously breached passwords.
- Resistance to advanced password-guessing techniques.
- Context-specific or predictable passwords.

A high score does not guarantee that a password is secure. This project should not be treated as a complete password-security assessment tool.

## 👨‍💻 Author

**Krishna Rungta**

MSc Cyber Security Student – Aston University, UK

**GitHub:** [github.com/krishna4222](https://github.com/krishna4222)

**LinkedIn:** [linkedin.com/in/krishna4222](https://linkedin.com/in/krishna4222)

---

⭐ *Learning, building and growing in cybersecurity every day.*
