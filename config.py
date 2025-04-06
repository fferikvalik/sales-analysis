# config.py
import os

# Определяем базовую директорию проекта
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# Пути к данным
DATA_DIR = os.path.join(BASE_DIR, 'data')
RAW_DATA_PATH = os.path.join(DATA_DIR, 'raw', 'sales_2023.csv')
PROCESSED_DATA_DIR = os.path.join(DATA_DIR, 'processed')

# Путь к базе данных SQLite
DB_PATH = os.path.join(BASE_DIR, 'sales.db')
