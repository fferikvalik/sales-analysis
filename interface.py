# interface.py
import argparse
import pandas as pd
import os

# Импортируем bootstrap для настройки sys.path
import bootstrap

# Импортируем функции для ETL-процесса и инициализации БД
from database.init_db import init_db
from etl.extract import extract_data
from etl.transform import clean_data
from etl.load import load_data
from config import DB_PATH, PROCESSED_DATA_DIR

def run_init_db():
    init_db()
    print("База данных и таблица 'sales' созданы успешно.")

def run_extract():
    df = extract_data()
    if df is not None:
        print("Извлеченные данные:")
        print(df.head())
    return df

def run_transform():
    # Извлекаем данные для трансформации
    df = extract_data()
    if df is None:
        return None
    cleaned_df = clean_data(df)
    
    # Создаем папку processed, если её нет
    os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)
    processed_csv_path = os.path.join(PROCESSED_DATA_DIR, 'sales_2023_cleaned.csv')
    
    # Сохраняем очищенные данные
    cleaned_df.to_csv(processed_csv_path, index=False)
    print(f"Очищенные данные сохранены в {processed_csv_path}")
    return cleaned_df

def run_load():
    # Загружаем очищенные данные из файла и записываем в БД
    processed_csv_path = os.path.join(PROCESSED_DATA_DIR, 'sales_2023_cleaned.csv')
    try:
        df = pd.read_csv(processed_csv_path)
    except Exception as e:
        print("Ошибка при чтении очищенного CSV:", e)
        return
    load_data(df)

def run_reset():
    # Удаляем файл базы данных, если он существует
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
        print("База данных удалена.")
    else:
        print("База данных не найдена.")
    # Создаем базу данных заново
    run_init_db()
    print("База данных приведена к исходному состоянию.")

def run_all():
    # Выполняем полный ETL-процесс
    run_init_db()
    run_extract()
    run_transform()
    run_load()

def main():
    parser = argparse.ArgumentParser(description="CLI для ETL приложения Sales Analysis")
    parser.add_argument("command", choices=["init", "extract", "transform", "load", "reset", "all"],
                        help=("Команда для выполнения: "
                              "init (инициализация БД), "
                              "extract (извлечение данных), "
                              "transform (очистка данных), "
                              "load (загрузка в БД), "
                              "reset (сброс базы данных), "
                              "all (все этапы)"))
    args = parser.parse_args()

    if args.command == "init":
        run_init_db()
    elif args.command == "extract":
        run_extract()
    elif args.command == "transform":
        run_transform()
    elif args.command == "load":
        run_load()
    elif args.command == "reset":
        run_reset()
    elif args.command == "all":
        run_all()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
