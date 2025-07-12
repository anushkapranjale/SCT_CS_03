def check_password_strength(password):
    length = False
    upper = False
    lower = False
    number = False
    special = False

    # Go through each character
    for char in password:
        if char.isupper():
            upper = True
        elif char.islower():
            lower = True
        elif char.isdigit():
            number = True
        elif not char.isalnum():
            special = True

    if len(password) >= 8:
        length = True

    # Count how many conditions are true
    score = 0
    if length:
        score += 1
    if upper:
        score += 1
    if lower:
        score += 1
    if number:
        score += 1
    if special:
        score += 1

    # Display results
    print("\nPassword Strength Check:")
    print("Length >= 8:", "✔️" if length else "❌")
    print("Uppercase Letter:", "✔️" if upper else "❌")
    print("Lowercase Letter:", "✔️" if lower else "❌")
    print("Number:", "✔️" if number else "❌")
    print("Special Character:", "✔️" if special else "❌")

    # Final strength rating
    if score == 5:
        print("\nOverall Strength: 💪 Very Strong")
    elif score == 4:
        print("\nOverall Strength: ✅ Strong")
    elif score == 3:
        print("\nOverall Strength: ⚠️ Moderate")
    else:
        print("\nOverall Strength: ❌ Weak")

# --- Main Program ---
pwd = input("Enter your password: ")
check_password_strength(pwd)
