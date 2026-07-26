# Password Strength Checker

passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]

special = "!@#$%^&*"

for password in passwords:

    print("\nChecking password:", password)

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in password:
        if ch.isupper():
            has_upper = True

        elif ch.islower():
            has_lower = True

        elif ch.isdigit():
            has_digit = True

        elif ch in special:
            has_special = True

    if len(password) >= 8 and has_upper and has_lower and has_digit and has_special:
        print("Strong Password")
    else:
        print("Weak Password")

        if len(password) < 8:
            print("- At least 8 characters required")

        if not has_upper:
            print("- Missing uppercase letter")

        if not has_lower:
            print("- Missing lowercase letter")

        if not has_digit:
            print("- Missing digit")

        if not has_special:
            print("- Missing special character")