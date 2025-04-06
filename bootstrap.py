# bootstrap.py
import sys
import os

# Добавляем родительскую папку (корень проекта) в sys.path,
# чтобы не дублировать этот код в каждом файле.
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
