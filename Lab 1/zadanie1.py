# Zadanie 1
# Napisz skrypt zliczający ilość plików w katalogu /dev (lub w dowolnym katalogu), 
# skorzystaj ze standardowej biblioteki - os

import os

def count_files_and_directories(directory):
    try:
        items = os.listdir(directory)
        file_count = sum(1 for item in items if os.path.isfile(os.path.join(directory, item)))
        dir_count = sum(1 for item in items if os.path.isdir(os.path.join(directory, item)))
        return file_count, dir_count
    except FileNotFoundError:
        return "Podany katalog nie istnieje."
    except PermissionError:
        return "Brak dostępu do podanego katalogu."

directory_path = r'C:\Users\grzen\Desktop\Jazda\Notepads'
file_count, dir_count = count_files_and_directories(directory_path)

print(f"Ilość plików w katalogu {directory_path}: {file_count}")
print(f"Ilość katalogów w katalogu {directory_path}: {dir_count}")