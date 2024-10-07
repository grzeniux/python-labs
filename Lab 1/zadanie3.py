# Zadanie 3
# Napisz skrypt usuwający z wejściowego ciągu tekstowego 
# (można plik wygenerować samemu lub ściągnąć np. z portalu informacyjnego) 
# wybrane słowa podane jako parametr wejściowy 

import os

def remove_words_from_text(text, words_to_remove):
    words = text.split()
    filtered_words = [word for word in words if word not in words_to_remove]
    filtered_text = ' '.join(filtered_words)
    return filtered_text

def remove_words_from_file(input_file, output_file, words_to_remove):
    try:
        if not os.path.exists(input_file):
            print(f"Plik {input_file} nie istnieje.")
            return
        
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        filtered_text = remove_words_from_text(text, words_to_remove)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(filtered_text)
        print(f"Przetworzony tekst został zapisany w pliku: {output_file}")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

input_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\input_zad3.txt'
output_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\output_zad3.txt'
words_to_remove = ['SIWEGO', 'mną'] 

remove_words_from_file(input_file, output_file, words_to_remove)
