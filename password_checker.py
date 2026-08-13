import re
import random
import string

def check_strength(password):
    score = 0
    tips = []

    if len(password) >= 12:
        score += 2
    elif len(password) >= 8:
        score += 1
    else:
        tips.append("Make it at least 12 characters")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add lowercase letters")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Add numbers")

    if re.search(r"[!@#$%^&*]", password):
        score += 1
    else:
        tips.append("Add special characters")

    if score >= 5:
        return "Very Strong", tips
    elif score >= 4:
        return "Strong", tips
    elif score >= 3:
        return "Medium", tips
    else:
        return "Weak", tips


def generate_password(length=16):
    chars = string.ascii_letters + string.digits + "!@#$%^&*"
    return ''.join(random.choice(chars) for _ in range(length))


print("=== Password Strength Checker ===")
print("Cybersecurity Portfolio Project\n")

while True:
    print("1. Check password")
    print("2. Generate password")
    print("3. Exit")

    choice = input("\nEnter choice (1-3): ")

    if choice == "1":
        pwd = input("Enter password: ")
        strength, tips = check_strength(pwd)
        print("\nStrength:", strength)
        if tips:
            print("Tips:")
            for t in tips:
                print("-", t)
        print()

    elif choice == "2":
        print("\nGenerated password:", generate_password())
        print()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice\n")
