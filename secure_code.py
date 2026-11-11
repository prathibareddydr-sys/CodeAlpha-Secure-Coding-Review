# CodeAlpha Cybersecurity Internship
# Task 3: Secure Coding Review
# Secure Version

import sqlite3
import hashlib
import os
import hmac

# Secure password hashing
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)

    hashed = hashlib.pbkdf2_hmac(
        "sha256",
        password.encode(),
        salt,
        100000
    )

    return salt, hashed


# Create database
connection = sqlite3.connect("users.db")
cursor = connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    username TEXT PRIMARY KEY,
    salt BLOB NOT NULL,
    password_hash BLOB NOT NULL
)
""")

# Get user input
username = input("Enter username: ")
password = input("Enter password: ")

# Check user using parameterized SQL query
cursor.execute(
    "SELECT salt, password_hash FROM users WHERE username = ?",
    (username,)
)

user = cursor.fetchone()

if user:
    salt, stored_hash = user
    _, entered_hash = hash_password(password, salt)

    if hmac.compare_digest(entered_hash, stored_hash):
        print("Login Successful!")
    else:
        print("Invalid username or password.")

else:
    # Register a new user securely
    salt, password_hash = hash_password(password)

    cursor.execute(
        "INSERT INTO users (username, salt, password_hash) VALUES (?, ?, ?)",
        (username, salt, password_hash)
    )

    connection.commit()
    print("Account created successfully!")

connection.close()