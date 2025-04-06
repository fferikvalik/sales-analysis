import sys
import os

# Добавляем родительскую папку (корень проекта) в sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# etl/transform.py
import pandas as pd
import os
from config import RAW_DATA_PATH, PROCESSED_DATA_DIR

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df['date'] = pd.to_datetime(df['date'], errors='coerce')
    df['total'] = df['quantity'] * df['price']
    cleaned_df = df.dropna()
    return cleaned_df

if __name__ == "__main__":
    # Создаем папку processed, если она отсутствует
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

    # Чтение исходного CSV
    df = pd.read_csv(RAW_DATA_PATH)
    cleaned_df = clean_data(df)
    
    # Сохраняем очищенные данные
    processed_csv_path = os.path.join(PROCESSED_DATA_DIR, 'sales_2023_cleaned.csv')
    cleaned_df.to_csv(processed_csv_path, index=False)
    print(f"Очищенные данные сохранены в {processed_csv_path}")
