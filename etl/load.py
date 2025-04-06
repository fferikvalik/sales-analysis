import sys
import os

# Добавляем родительскую папку (корень проекта) в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# etl/load.py
import sqlite3
import pandas as pd
from config import DB_PATH, PROCESSED_DATA_DIR
import os

def load_data(df: pd.DataFrame, clear_table: bool = False):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    try:
        if clear_table:
            cursor.execute("DELETE FROM sales;")
            conn.commit()
            print("Таблица 'sales' очищена перед загрузкой данных.")
        
        # Загружаем данные в таблицу 'sales'
        df.to_sql('sales', conn, if_exists='append', index=False)
        print("Данные успешно загружены в базу данных.")
    except sqlite3.IntegrityError as e:
        print("Ошибка при загрузке данных:", e)
    finally:
        conn.close()

if __name__ == "__main__":
    processed_csv = os.path.join(PROCESSED_DATA_DIR, 'sales_2023_cleaned.csv')
    try:
        df = pd.read_csv(processed_csv)
        # Установите clear_table=True, если хотите очистить таблицу перед загрузкой
        load_data(df, clear_table=True)
    except Exception as e:
        print("Ошибка при чтении очищенного CSV:", e)
