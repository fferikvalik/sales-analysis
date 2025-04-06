import sys
import os

# Добавляем родительскую папку (корень проекта) в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# database/init_db.py
import sqlite3
from config import DB_PATH

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    # Создаем таблицу sales, если она не существует
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS sales (
            order_id INTEGER PRIMARY KEY,
            date TEXT,
            product TEXT,
            quantity INTEGER,
            price REAL,
            region TEXT,
            total REAL
        );
    ''')
    conn.commit()
    conn.close()

if __name__ == "__main__":
    init_db()
    print("База данных и таблица 'sales' созданы успешно.")
