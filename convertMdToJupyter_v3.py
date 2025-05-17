import nbformat
import re
from pathlib import Path

def convert_to_ipynb(input_file, output_file):
    """
    Konwertuje plik Markdown na plik Jupyter Notebook (.ipynb),
    poprawnie dzieląc nagłówki, kod i tekst.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Tworzymy nowy notebook
    notebook = nbformat.v4.new_notebook()
    cells = []

    # Wzorzec do rozpoznawania bloków kodu i nagłówków
    pattern = r"(#+ .+|\n```[a-zA-Z0-9]*\n[\s\S]*?\n```)"
    parts = re.split(pattern, content)

    for part in parts:
        if not part.strip():
            continue  # Pomijamy puste fragmenty

        # Sprawdzamy, czy to jest blok kodu
        code_match = re.match(r"\n```([a-zA-Z0-9]*)\n([\s\S]*?)\n```", part)
        if code_match:
            language = code_match.group(1) or "python"  # Domyślnie Python
            code_content = code_match.group(2).strip()
            cells.append(nbformat.v4.new_code_cell(code_content))
            continue

        # Sprawdzamy, czy to jest nagłówek (np. #, ##, ###)
        header_match = re.match(r"(#+) (.+)", part)
        if header_match:
            # Wrzucamy nagłówki do osobnej komórki markdown
            cells.append(nbformat.v4.new_markdown_cell(part.strip()))
            continue

        # Jeśli to nie nagłówek ani kod, traktujemy jako zwykły tekst Markdown
        if part.strip():
            cells.append(nbformat.v4.new_markdown_cell(part.strip()))

    # Dodajemy komórki do notebooka
    notebook.cells = cells

    # Zapisujemy notebook do pliku .ipynb
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

if __name__ == "__main__":
    # Pobierz wszystkie pliki .md w katalogu
    md_files = list(Path('.').glob("*.md"))

    for md_file in md_files:
        ipynb_file = md_file.with_suffix(".ipynb")
        print(f"Konwertuję {md_file} → {ipynb_file}...")
        convert_to_ipynb(md_file, ipynb_file)

    print("✅ Konwersja zakończona!")
