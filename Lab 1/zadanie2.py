# Zadanie 2
# Napisz rekurencyjne przejście drzewa katalogów i wypisanie plików, 
# które znajdują się w podanym jako parametr katalogu

import os

def list_files_recursive(directory):
    try:
        items = os.listdir(directory)
        for item in items:
            full_path = os.path.join(directory, item)
            if os.path.isdir(full_path):
                print(f"Katalog: {full_path}")
                list_files_recursive(full_path)
            else:
                print(f"Plik: {full_path}")
    except FileNotFoundError:
        print(f"Katalog {directory} nie istnieje.")
    except PermissionError:
        print(f"Brak dostępu do katalogu {directory}.")

directory_path = r'C:\Users\grzen\Desktop\Jazda\Notepads'
list_files_recursive(directory_path)

