#!/bin/bash

echo "🔄 Aktualizacja listy pakietów..."
sudo apt update && sudo apt upgrade -y

echo "🧹 Usuwanie niepotrzebnych pakietów (autoremove)..."
sudo apt autoremove -y

echo "🧹 Czyszczenie cache APT..."
sudo apt autoclean -y
sudo apt clean -y

echo "🧹 Czyszczenie katalogu tymczasowego /tmp..."
sudo find /tmp -type f -atime +7 -delete

echo "🧹 Czyszczenie starych logów systemowych (starsze niż 7 dni)..."
sudo journalctl --vacuum-time=7d

echo "🧹 Czyszczenie cache Pythona, Pip i Jupyter..."
rm -rf ~/.cache/pip
rm -rf ~/.cache/pypoetry
rm -rf ~/.local/share/jupyter/runtime

echo "📊 Sprawdzanie zajętości dysku przed i po..."

echo "📁 Rozmiar katalogu / przed czyszczeniem:"
sudo du -sh /

echo "✅ Czyszczenie zakończone!"
