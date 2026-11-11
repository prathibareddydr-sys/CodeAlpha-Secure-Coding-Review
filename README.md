Secure Coding Review

CodeAlpha Cybersecurity Internship – Task 3

Project Overview

This project demonstrates common security vulnerabilities in Python applications and shows how to fix them using secure coding practices.

Objectives

- Identify security vulnerabilities.
- Understand insecure coding practices.
- Implement secure coding techniques.
- Improve application security.

Vulnerabilities Identified

1. Hardcoded credentials.
2. SQL Injection vulnerability.
3. Plain-text password storage.

Security Improvements

1. Used parameterized SQL queries to prevent SQL injection.
2. Used PBKDF2-HMAC-SHA256 password hashing with a random salt.
3. Used secure password verification with "hmac.compare_digest".
4. Removed hardcoded login credentials.

Technologies Used

- Python
- SQLite
- VS Code

Project Structure

- "vulnerable/" – Contains the vulnerable Python program.
- "secure/" – Contains the improved secure Python program.
- "screenshots/" – Contains project screenshots.

Testing Results

- Account creation successful.
- Correct password login successful.
- Incorrect password rejected.

Conclusion

This project helped me understand common software security vulnerabilities and implement secure coding practices to reduce security risks.

Internship: CodeAlpha Cybersecurity Internship
Task: Secure Coding Review