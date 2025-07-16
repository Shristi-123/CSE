import re

def check_password(password):
    tips = []
    score = 0

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Password should be at least 8 characters long.")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Include at least one uppercase letter.")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Include at least one lowercase letter.")

    if re.search(r"[0-9]", password):
        score += 1
    else:
        tips.append("Include at least one number.")

    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        score += 1
    else:
        tips.append("Include at least one special character.")

    if score >= 4:
        return "Strong ", tips
    elif score >= 3:
        return "Moderate ", tips
    else:
        return "Weak ", tips

def main():
    print("Password Strength Checker")
    pwd = input("Enter your password: ")
    level, advice = check_password(pwd)

    print("\nStrength:", level)
    if advice:
        print("Suggestions:")
        for tip in advice:
            print("-", tip)

if __name__ == "__main__":
    main()



