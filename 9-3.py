ru_en_dict = {}

with open('en-ru.txt', 'r', encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        if not line:
            continue
            
        parts = line.replace(' – ', ' - ').split(' - ')
        if len(parts) == 2:
            en_word = parts[0].strip()
            ru_words = parts[1].split(',')
            
            for ru_word in ru_words:
                ru_word = ru_word.strip()
                if ru_word not in ru_en_dict:
                    ru_en_dict[ru_word] = []
                ru_en_dict[ru_word].append(en_word)

with open('ru-en.txt', 'w', encoding='utf-8') as file:
    for ru_word in sorted(ru_en_dict.keys()):
        en_translations = ', '.join(sorted(ru_en_dict[ru_word]))
        file.write(f"{ru_word} – {en_translations}\n")
