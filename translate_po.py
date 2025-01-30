import os
from googletrans import Translator

# Configurar los idiomas a traducir (agrega más si necesitas)
LANGUAGES = ['es', 'de', 'fr', 'it', 'pt', 'en']

def translate_po_file(po_file, target_language):
    translator = Translator()

    with open(po_file, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    translated_lines = []
    translate_next = False

    for line in lines:
        if line.startswith('msgid'):
            original_text = line.split('"')[1]
            translate_next = True
            translated_lines.append(line)
        elif line.startswith('msgstr') and translate_next:
            translated_text = translator.translate(original_text, dest=target_language).text
            translated_lines.append(f'msgstr "{translated_text}"\n')
            translate_next = False
        else:
            translated_lines.append(line)

    with open(po_file, 'w', encoding='utf-8') as file:
        file.writelines(translated_lines)

# Traducir todos los archivos .po en /locale/
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOCALE_DIR = os.path.join(BASE_DIR, 'locale')

for lang in LANGUAGES:
    po_file_path = os.path.join(LOCALE_DIR, lang, 'LC_MESSAGES', 'django.po')
    if os.path.exists(po_file_path):
        print(f"Traduciendo {lang}...")
        translate_po_file(po_file_path, lang)
    else:
        print(f"⚠ No se encontró el archivo {po_file_path}")
