import os
import re
import shutil
import argparse

def rename_files(directory):
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)

        if os.path.isfile(filepath):
            new_filename = process_filename(filename)
            new_filepath = os.path.join(directory, new_filename)

            # Sprawdzamy, czy nowa nazwa pliku różni się od starej
            if new_filename != filename:
                print(f"Zmiana nazwy pliku: {filename} -> {new_filename}")
                shutil.move(filepath, new_filepath)
            else:
                print(f"Brak zmian w nazwie pliku: {filename}")

def process_filename(filename):
    # Wyrażenie regularne dla nazwy pliku z Imieniem i Nazwiskiem autora
    pattern_author = re.compile(r'(.+) \((\w) (\w+)\) \(.*\)\.(pdf|mobi|epub)')

    # Wyrażenie regularne dla nazwy pliku z dodatkową nazwą
    pattern_additional = re.compile(r'(.+) \((.*)\) \(.*\)\.(pdf|mobi|epub)')

    match_author = pattern_author.match(filename)
    match_additional = pattern_additional.match(filename)

    if match_author:
        title = match_author.group(1)
        first_name = match_author.group(2)
        last_name = match_author.group(3)
        extension = match_author.group(4)
        new_filename = f"{first_name.upper()}. {last_name} - {title}.{extension}"
    elif match_additional:
        title = match_additional.group(1)
        additional_name = match_additional.group(2)
        extension = match_additional.group(3)
        new_filename = f"{additional_name} - {title}.{extension}"
    else:
        # Jeśli nazwa pliku nie pasuje do żadnego z powyższych wzorców
        new_filename = filename

    return new_filename

def main():
    parser = argparse.ArgumentParser(description='Script for renaming files.')
    parser.add_argument('directory', metavar='directory', type=str, help='Path to the directory with files')

    args = parser.parse_args()
    rename_files(args.directory)

if __name__ == "__main__":
    main()