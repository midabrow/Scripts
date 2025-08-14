from bs4 import BeautifulSoup

# Load English definitions and Polish translations
def load_definitions_and_translations(definitions_file, translations_file):
    with open(definitions_file, 'r', encoding='utf-8') as file:
        definitions = [line.strip() for line in file.readlines()]

    with open(translations_file, 'r', encoding='utf-8') as file:
        translations = [line.strip() for line in file.readlines()]

    # Create a dictionary mapping English definitions to Polish translations
    translation_map = dict(zip(definitions, translations))
    return translation_map

# Replace definitions in the original HTML file with translations
def replace_definitions(html_file, translation_map, output_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

    for definition_tag in soup.find_all("div", class_="aw-definition"):
        english_definition = definition_tag.get_text(strip=True)
        if english_definition in translation_map:
            definition_tag.string = translation_map[english_definition]

    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(str(soup))

# File paths (update these as necessary)
definitions_file = '/home/midabrow/Pulpit/Nauka_Python/Skrypty/anki-definitions.txt'
translations_file = '/home/midabrow/Pulpit/Nauka_Python/Skrypty/anki-translations.txt'
original_html_file = '/home/midabrow/Pulpit/Nauka_Python/Skrypty/anki-import.txt'
output_html_file = 'anki-translated-final.txt'

# Load translation map and apply replacements
translation_map = load_definitions_and_translations(definitions_file, translations_file)
replace_definitions(original_html_file, translation_map, output_html_file)

print(f"Translated file saved as {output_html_file}")
