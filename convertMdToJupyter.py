import argparse
import pypandoc
import nbformat
import re
from pathlib import Path


def convert_to_ipynb(input_file, output_file):
    """
    Converts a Markdown file to a Jupyter Notebook file using pypandoc and nbformat.
    """
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Utwórz nowy notebook
    notebook = nbformat.v4.new_notebook()
    cells = []
    
    # Podziel zawartość na sekcje tekstu i kodu
    parts = re.split(r"(```sql\n(.*?)\n```)", content, flags=re.DOTALL)
    
    for i, part in enumerate(parts):
        if i % 3 == 0:
            # Tekst bez kodu
            if part.strip():
                cells.append(nbformat.v4.new_markdown_cell(part.strip()))
        elif i % 3 == 2:
            # Kod w Pythonie
            code = part.strip()
            # Tworzymy komórkę z kodem i ustawiamy język na SQL
            code_cell = nbformat.v4.new_code_cell(code)
            code_cell.metadata['language'] = 'sql'  # Ustawienie języka na SQL
            cells.append(code_cell)
    
    # Dodaj komórki do notebooka
    notebook.cells = cells

    # Zapisz notebook do pliku .ipynb
    with open(output_file, 'w', encoding='utf-8') as f:
        nbformat.write(notebook, f)
if __name__ == "__main__":
    # Create the command-line interface
    parser = argparse.ArgumentParser(description="Convert a Markdown file to a Jupyter Notebook file.")
    parser.add_argument("input_file", help="the input Markdown file path")
    parser.add_argument("output_file", help="the output Jupyter Notebook file path")
    args = parser.parse_args()

    # Convert the input file to a Jupyter Notebook file
    convert_to_ipynb(args.input_file, args.output_file)
