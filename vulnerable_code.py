# CodeAlpha Cybersecurity Internship
# Task 3: Secure Coding Review

username = input("Enter username: ")
password = input("Enter password: ")

# Vulnerability 1: Hardcoded credentials
if username == "admin" and password == "admin123":
    print("Login Successful!")
else:
    print("Invalid username or password.")

# Vulnerability 2: SQL Injection risk
query = "SELECT * FROM users WHERE username = '" + username + "'"
print("Generated SQL Query:", query)

# Vulnerability 3: Plain-text password storage
stored_password = password
print("Stored password:", stored_password)