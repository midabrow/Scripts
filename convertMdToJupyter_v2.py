import pypandoc
import nbformat
import re
from pathlib import Path

def convert_to_ipynb(input_file, output_file):
    """
    Converts a Markdown file to a Jupyter Notebook file using nbformat.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Utwórz nowy notebook
    notebook = nbformat.v4.new_notebook()
    cells = []
    
    # Podziel zawartość na sekcje tekstu i kodu
    parts = re.split(r"(```python\n(.*?)\n```)", content, flags=re.DOTALL)
    
    for i, part in enumerate(parts):
        if i % 3 == 0:
            # Tekst bez kodu
            if part.strip():
                cells.append(nbformat.v4.new_markdown_cell(part.strip()))
        elif i % 3 == 2:
            # Kod w Pythonie
            code = part.strip()
            cells.append(nbformat.v4.new_code_cell(code))
    
    # Dodaj komórki do notebooka
    notebook.cells = cells

    # Zapisz notebook do pliku .ipynb
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)

if __name__ == "__main__":
    # Wybierz wszystkie pliki .md w bieżącym katalogu
    md_files = list(Path('.').glob("*.md"))
    
    for md_file in md_files:
        # Nazwa pliku .ipynb jest taka sama jak .md
        ipynb_file = md_file.with_suffix(".ipynb")
        print(f"Converting {md_file} to {ipynb_file}")
        
        # Konwersja pliku
        convert_to_ipynb(md_file, ipynb_file)

