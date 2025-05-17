import os
import sys

def change_numerations(directory, increment):
    # Lista folderów w katalogu
    folders = sorted([f for f in os.listdir(directory) if os.path.isdir(os.path.join(directory, f))])

    for folder in folders:
        # Sprawdzamy, czy folder ma numer na początku
        parts = folder.split('_', 1)
        if parts[0].isdigit():
            # Zmieniamy numerację
            new_number = str(int(parts[0]) + increment).zfill(2)
            new_folder = f"{new_number}_{parts[1]}"
            # Ścieżki do starych i nowych folderów
            old_folder_path = os.path.join(directory, folder)
            new_folder_path = os.path.join(directory, new_folder)

            # Zmieniamy nazwę folderu
            os.rename(old_folder_path, new_folder_path)
            print(f"Zmiana: {folder} -> {new_folder}")

if __name__ == "__main__":
    # Argumenty wejściowe
    if len(sys.argv) != 3:
        print("Użycie: python3 changeNumerations.py <katalog> <inkrement>")
        sys.exit(1)
    
    directory = sys.argv[1]
    increment = int(sys.argv[2])

    # Uruchomienie funkcji zmieniającej numerację
    change_numerations(directory, increment)

