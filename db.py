import sqlite3
import json

DATABASE = 'users.db'

# Initialize database and tables
def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            phone INTEGER
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Home (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            address TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Work (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER,
            address TEXT,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    ''')

    conn.commit()
    conn.close()

# Get all users with home and work addresses
def get_all_users_full():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT 
            users.id,
            users.name,
            users.phone,
            COALESCE(Home.address, '') AS home_address,
            COALESCE(Work.address, '') AS work_address
        FROM users
        LEFT JOIN Home ON users.id = Home.user_id
        LEFT JOIN Work ON users.id = Work.user_id
    ''')

    rows = cursor.fetchall()
    conn.close()

    if not rows:
        return [], "Add user please"

    users = []
    for row in rows:
        users.append({
            'id': row[0],
            'name': row[1],
            'phone': row[2],
            'home_address': row[3],
            'work_address': row[4]
        })

    return users, None
