password = input("Enter your password: ").strip()

if len(password) < 6:
    password_strength = "Weak"
elif len(password) < 8:
    password_strength = "Medium"
else:
    password_strength = "Strong"

print(f"Your password is {password_strength}")