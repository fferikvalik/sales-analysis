import sys
import os

# Добавляем родительскую папку (корень проекта) в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# etl/extract.py
import pandas as pd
from config import RAW_DATA_PATH

def extract_data():
    try:
        # Чтение исходного CSV файла
        df = pd.read_csv(RAW_DATA_PATH)
        print("Данные успешно загружены.")
        return df
    except Exception as e:
        print(f"Ошибка при чтении CSV: {e}")
        return None

if __name__ == "__main__":
    df = extract_data()
    if df is not None:
        print(df.head())
