import sqlite3
from datetime import datetime
import json

class MemoryStore:
    def __init__(self, db_path = "memory_store.db"):
        self.conn = sqlite3.connect(db_path, check_same_thread = False)
        self.create_table()
    
    def create_table(self):
        self.conn.execute('''
            CREATE TABLE IF NOT EXISTS memory (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                source TEXT,
                type TEXT,
                intent TEXT,
                timestamp TEXT,
                extracted_fields TEXT,
                thread_id TEXT
            )
        ''')
        self.conn.commit()

    def save(self, data):
        self.conn.execute('''
            INSERT INTO memory (source, type, intent, timestamp, extracted_fields, thread_id)
            VALUES (?, ?, ?, ?, ?, ?)
            ''', (
                data.get('source'),
                data.get('type'),
                data.get('intent'),
                data.get('timestamp', str(datetime.now())),
                str(data.get('extracted_fields')),
                data.get('thread_id')
            )
        )
        self.conn.commit()

    def load_all(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM memory')
        rows = cursor.fetchall()
        logs = []

        for row in rows:
            extracted = json.loads(row[4]) if row[4] else {}
            logs.append({
                'id' : row[0],
                'source' : row[1],
                'type' : row[2],
                'intent' : row[3],
                'extracted_fields' : extracted,
                'thread_id' : row[5],
                'timestamp' : row[6]
            })
        return logs