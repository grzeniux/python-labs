# Zadanie 3
# Napisz skrypt zmieniający w podanym ciągu wejściowym 
# (można plik wygenerować samemu lub sciągnąć np. z portalu informacyjnego) 
# wybrane słowa innymi slowami (podanymi w strukturze typu słownikowego) 
# podanymi jako parametr wejściowy funkcji

import os

def replace_words_in_text(text, replacement_dict):
    words = text.split()
    replaced_words = [replacement_dict.get(word, word) for word in words]
    replaced_text = ' '.join(replaced_words)
    return replaced_text

def replace_words_in_file(input_file, output_file, replacement_dict):
    try:
        if not os.path.exists(input_file):
            print(f"Plik {input_file} nie istnieje.")
            return
        
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        replaced_text = replace_words_in_text(text, replacement_dict)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(replaced_text)
        print(f"Przetworzony tekst został zapisany w pliku: {output_file}")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

input_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\input_zad3.txt'
output_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\output_zad4.txt'
replacement_dict = {
    'mną': 'studentem',  
    'sól': 'pieprz'  
}  

replace_words_in_file(input_file, output_file, replacement_dict)