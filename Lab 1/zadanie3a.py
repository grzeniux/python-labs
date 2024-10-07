# Zadanie 3
# Wykonaj to zadanie wykorzystując pakiet wyrażeń regularnych - re
# Napisz skrypt usuwający z wejściowego ciągu tekstowego 
# (można plik wygenerować samemu lub ściągnąć np. z portalu informacyjnego) 
# wybrane słowa podane jako parametr wejściowy 

import re
import os

def remove_words_with_regex(text, words_to_remove):
    pattern = r'\b(?:' + '|'.join(re.escape(word) for word in words_to_remove) + r')\b'
    cleaned_text = re.sub(pattern, '', text)
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text

def remove_words_from_file(input_file, output_file, words_to_remove):
    try:
        if not os.path.exists(input_file):
            print(f"Plik {input_file} nie istnieje.")
            return
        
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        cleaned_text = remove_words_with_regex(text, words_to_remove)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(cleaned_text)
        print(f"Przetworzony tekst został zapisany w pliku: {output_file}")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

input_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\input_zad3.txt'
output_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\output_zad3a.txt'
words_to_remove = ['SIWEGO', 'mną'] 

remove_words_from_file(input_file, output_file, words_to_remove)