# Zadanie 4a
# Wykonaj to zadanie wykorzystując pakiet wyrażeń regularnych - re
# Napisz skrypt zmieniający w podanym ciągu wejściowym 
# (można plik wygenerować samemu lub sciągnąć np. z portalu informacyjnego) 
# wybrane słowa innymi slowami (podanymi w strukturze typu słownikowego) 
# podanymi jako parametr wejściowy funkcji

import re
import os

def replace_words_with_regex(text, replacement_dict):
    pattern = r'\b(' + '|'.join(re.escape(word) for word in replacement_dict.keys()) + r')\b'
    
    def replace_match(match):
        return replacement_dict[match.group(0)]
    replaced_text = re.sub(pattern, replace_match, text)
    return replaced_text

def replace_words_in_file(input_file, output_file, replacement_dict):
    try:
        if not os.path.exists(input_file):
            print(f"Plik {input_file} nie istnieje.")
            return
        
        with open(input_file, 'r', encoding='utf-8') as file:
            text = file.read()
        replaced_text = replace_words_with_regex(text, replacement_dict)
        
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write(replaced_text)
        print(f"Przetworzony tekst został zapisany w pliku: {output_file}")
    
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

input_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\input_zad3.txt'
output_file = r'C:\Users\grzen\Desktop\Jazda\Studia\Sem7\Python\python-labs\Lab 1\output_zad4a.txt'
replacement_dict = {
    'mną': 'studentem',  
    'sól': 'pieprz'  
}  

replace_words_in_file(input_file, output_file, replacement_dict)