import sqlite3

def setup_database():
    conn = sqlite3.connect("game_history.db")
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS game_results (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            word TEXT,
            result TEXT,
            attempts INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    conn.commit()
    conn.close()

def save_game_result(word, result, attempts):
    conn = sqlite3.connect("game_history.db")
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO game_results (word, result, attempts)
        VALUES (?, ?, ?)
    ''', (word, result, attempts))
    conn.commit()
    conn.close()

setup_database()  # Call once to set up DB
