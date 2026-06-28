from fastapi import FastAPI
import sqlite3
app = FastAPI(title="SQL Injection Demo")
def init_db():
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS users (
                           id INTEGER PRIMARY KEY,
                           username TEXT,
                           password TEXT 
                           )
        """)
    cursor.execute("INSERT OR IGNORE INTO users VALUES (1, 'admin', 'secret')")
    cursor.execute("INSERT OR IGNORE INTO users VALUES (2, 'user', 'password')")
    conn.commit()
    conn.close()

init_db()

@app.post("/login/vulnerable")
def vulnerable_login(username: str, password: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    query = f"SELECT * FROM users WHERE username = '{username}'AND password='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"status": "success", "message": f"Welcome {username}!" }
    return {"status": "failed", "message": "Invalid credentials"}

@app.post("/login/secure")
def secure_login(username: str, password: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE username =? AND password=?",
        (username, password)
    )
    user = cursor.fetchone()
    conn.close()
    if user:
        return {"status": "success", "message": f"Welcome {username}!" }
    return {"status": "failed", "message": "Invalid credentials"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)