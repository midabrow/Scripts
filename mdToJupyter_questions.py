import os
import sys
import nbformat
import re

def process_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Wyodrębnij bloki (z uwzględnieniem bloków kodu SQL)
    blocks = re.split(r"(```sql.*?```|\n\n)", content, flags=re.DOTALL)

    # Utwórz nowy notebook
    notebook = nbformat.v4.new_notebook()
    for block in blocks:
        block = block.strip()
        if not block:
            continue
        if block.startswith("```sql"):
            # Przetwarzanie bloku SQL
            sql_code = block[6:-3].strip()  # Usuwa ```sql i ```
            cell = nbformat.v4.new_code_cell(sql_code)
        else:
            # Przetwarzanie zwykłego tekstu Markdown
            cell = nbformat.v4.new_markdown_cell(block)
        notebook.cells.append(cell)
    
    # Zapisz plik .ipynb
    output_file = os.path.splitext(file_path)[0] + ".ipynb"
    with open(output_file, "w", encoding="utf-8") as f:
        nbformat.write(notebook, f)
    print(f"Przetworzono: {file_path} -> {output_file}")

def process_all_markdown_files():
    for file_name in os.listdir():
        if file_name.endswith(".md"):
            process_markdown_file(file_name)

def main():
    if len(sys.argv) == 2:
        # Przetwarzanie jednego pliku
        file_path = sys.argv[1]
        if os.path.exists(file_path) and file_path.endswith(".md"):
            process_markdown_file(file_path)
        else:
            print("Podano nieprawidłowy plik Markdown.")
    else:
        # Przetwarzanie wszystkich plików .md w katalogu
        print("Przetwarzanie wszystkich plików Markdown w bieżącym katalogu...")
        process_all_markdown_files()

if __name__ == "__main__":
    main()
