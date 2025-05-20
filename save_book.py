import json
import os

FILE_PATH = "books.json"

def load_books():
    if os.path.exists(FILE_PATH):
        try:
            with open(FILE_PATH, "r") as file:
                return json.load(file)
        except json.JSONDecodeError:
            print("File rusak atau kosong. Memulai dengan katalog kosong.")
            return []
    return []

def save_books(books):
    try:
        with open(FILE_PATH, "w") as file:
            json.dump(books, file, indent=4)
    except Exception as e:
        print(f"Gagal menyimpan data: {e}")
