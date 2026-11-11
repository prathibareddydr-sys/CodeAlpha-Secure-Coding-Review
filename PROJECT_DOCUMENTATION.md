PROJECT DOCUMENTATION

1. Project Title

Secure Coding Review

2. Internship Details

- Organization: CodeAlpha
- Domain: Cybersecurity
- Task: Task 3 – Secure Coding Review

3. Introduction

Secure coding is the practice of writing programs that protect applications and user information from security threats.

This project demonstrates common vulnerabilities in Python code and provides improved solutions using secure coding techniques.

4. Problem Statement

Insecure applications may contain hardcoded credentials, SQL injection vulnerabilities, and unsafe password storage methods. These weaknesses can allow unauthorized access and expose sensitive information.

5. Vulnerabilities Identified

5.1 Hardcoded Credentials

Storing usernames and passwords directly in source code can expose login information.

5.2 SQL Injection

Building SQL queries by joining user input directly into query strings can allow malicious SQL input.

5.3 Plain-text Password Storage

Storing passwords without hashing exposes user credentials if the database is accessed by an unauthorized person.

6. Security Improvements

6.1 Parameterized Queries

Used parameterized SQL queries with placeholders to prevent SQL injection.

6.2 Password Hashing

Used PBKDF2-HMAC-SHA256 with a random salt to securely store password hashes.

6.3 Secure Password Verification

Used "hmac.compare_digest()" to compare password hashes safely.

7. Technologies Used

- Python
- SQLite
- VS Code

8. Testing and Results

The secure program was tested with the following cases:

1. Account creation – Successful.
2. Login with the correct password – Successful.
3. Login with an incorrect password – Rejected.

9. Project Structure

- vulnerable/ – Contains the vulnerable Python code.
- secure/ – Contains the improved secure Python code.
- screenshots/ – Contains screenshots of the implementation and testing.
- README.md – Provides a project overview.
- PROJECT_DOCUMENTATION.md – Provides detailed project documentation.

10. Conclusion

This project helped identify common security vulnerabilities and understand how secure coding practices can improve application security.

The implementation demonstrates the importance of parameterized SQL queries, password hashing, and secure authentication.

11. Learning Outcomes

- Understood common coding vulnerabilities.
- Learned basic SQL injection prevention.
- Practised password hashing.
- Improved Python programming and security knowledge.