def assess_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("At least 8 characters needed.")
    if any(c.islower() for c in password):
        score += 1
    else:
        feedback.append("Add lowercase letters.")
    if any(c.isupper() for c in password):
        score += 1
    else:
        feedback.append("Add uppercase letters.")
    if any(c.isdigit() for c in password):
        score += 1
    else:
        feedback.append("Add numbers.")
    if any(not c.isalnum() for c in password):
        score += 1
    else:
        feedback.append("Add special characters.")

    levels = ["Very Weak", "Weak", "Medium", "Strong", "Very Strong", "Excellent"]
    strength = levels[score if score < len(levels) else len(levels) - 1]

    return {"Strength": strength, "Feedback": feedback if feedback else ["No improvements needed!"]}

user_password = input("Enter a password to assess: ")
result = assess_password_strength(user_password)

print("Strength:", result["Strength"])
print("Feedback:")
for f in result["Feedback"]:
    print("-", f)
