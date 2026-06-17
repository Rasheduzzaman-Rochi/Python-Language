correct_password = "12345"
attempts = [input("Enter your password: ")]

for password in attempts:
    if password == correct_password:
        print("Access granted.")
        break
    else:
        print("Access denied. Try again.")