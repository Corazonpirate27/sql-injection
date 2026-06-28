![Python](https://img.shields.io/badge/Python-3.12-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-latest-green)
![SQLite](https://img.shields.io/badge/SQLite-3-lightblue)
![OWASP](https://img.shields.io/badge/OWASP-Top%2010-red)
![License](https://img.shields.io/badge/License-MIT-yellow)

# SQL Injection Demo

A FastAPI application demonstrating SQL injection attacks 
and how to prevent them using parameterized queries.

## What it does
- Demonstrates vulnerable login endpoint
- Demonstrates secure login endpoint
- Shows SQL injection attack in action
- Shows how parameterized queries block the attack

## Tools used
- Python 3.12
- FastAPI
- SQLite3
- Uvicorn

## How to run
pip install fastapi uvicorn
python app.py

## API endpoints
- POST /login/vulnerable → Vulnerable to SQL injection
- POST /login/secure    → Protected with parameterized queries

## The attack
Typing admin'-- as username bypasses password check:
- Vulnerable: Returns success without correct password!
- Secure: Returns invalid credentials — attack blocked!

## The fix
Vulnerable:
query = f"SELECT * FROM users WHERE username='{username}'"

Secure:
cursor.execute(
    "SELECT * FROM users WHERE username=? AND password=?",
    (username, password)
)

## Real world impact
SQL injection is #1 on OWASP Top 10 for 20+ years.
One vulnerable line = complete authentication bypass!

## Author
Corazonpirate27
