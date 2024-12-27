import sqlite3


class Database:
    def __init__(self, path: str):
        self.path = path

    def create_tables(self):
        with sqlite3.connect(self.path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS complaints (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT,
                    phone_num TEXT,
                    complaint TEXT
                )
            """)
            conn.commit()

    def save_complaints(self, data: dict):
        with sqlite3.connect(self.path) as conn:
            conn.execute('''
                INSERT INTO complaints (name, phone_num, complaint)
                VALUES (?, ?, ?)
            ''',
            (data['name'], data['phone_num'], data['complaint'])
            )
            conn.commit()