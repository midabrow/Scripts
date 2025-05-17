#!/bin/bash

echo "🔍 Wyszukiwanie pakietów zainstalowanych jednocześnie przez conda i pip..."

# Tworzenie tymczasowych plików z listami
conda list | awk '{print $1}' | sort > /tmp/conda_list.txt
pip list --format=columns | awk 'NR>2 {print $1}' | sort > /tmp/pip_list.txt

# Znalezienie wspólnych pakietów
comm -12 /tmp/conda_list.txt /tmp/pip_list.txt > /tmp/common_packages.txt

echo "📦 Pakiety do usunięcia z pip:"
cat /tmp/common_packages.txt

echo "❓ Czy na pewno chcesz usunąć te pakiety z pip? (y/n)"
read confirm

if [[ $confirm == "y" || $confirm == "Y" ]]; then
    xargs pip uninstall -y < /tmp/common_packages.txt
    echo "✅ Usunięto powielone pakiety pip."
    echo "🧹 Czyszczenie cache pip..."
    pip cache purge
    echo "✅ Gotowe! Środowisko oczyszczone."
else
    echo "❌ Operacja anulowana przez użytkownika."
fi

# Czyszczenie plików tymczasowych
rm /tmp/conda_list.txt /tmp/pip_list.txt /tmp/common_packages.txt
