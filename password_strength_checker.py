import re

def check_password_strength(password):
    score = 0
    remarks = ""

    length = len(password)

    if length < 6:
        remarks = "Password too short!"
        return "Very Weak", remarks
    elif length < 8:
        score += 1
    elif length <= 10:
        score += 2
    else:
        score += 3
    lower_count = len(re.findall("[a-z]", password))
    if lower_count >= 2:
        score += 1

    upper_count = len(re.findall("[A-Z]", password))
    if upper_count >= 2:
        score += 1

    digit_count = len(re.findall("[0-9]", password))
    if digit_count >= 2:
        score += 1

    symbol_count = len(re.findall("[!@#$%^&*(),.?\":{}|<>]", password))
    if symbol_count >= 1:
        score += 1

    if score <= 2:
        strength = "Weak"
        remarks = "Try adding more characters, numbers, and symbols."
    elif score <= 4:
        strength = "Medium"
        remarks = "Pretty good! Add more mix of upper/lower and symbols."
    elif score <= 6:
        strength = "Strong"
        remarks = "Nice! Your password is strong."
    else:
        strength = "Very Strong"
        remarks = "Excellent! Hard to crack password."

    return strength, remarks

password = input("Enter your password: ")
strength, remarks = check_password_strength(password)

print(f"\nPassword Strength: {strength}")
print(f"Feedback: {remarks}")
