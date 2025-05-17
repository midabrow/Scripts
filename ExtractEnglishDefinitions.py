from bs4 import BeautifulSoup

# Load the content of the file
file_path = '/home/midabrow/Pulpit/Nauka_Python/Skrypty/anki-import.txt'
with open(file_path, 'r', encoding='utf-8') as file:
    html_content = file.read()

# Parse the HTML content
soup = BeautifulSoup(html_content, 'html.parser')

# Extract all definitions from the HTML file
definitions = [tag.get_text(strip=True) for tag in soup.find_all("div", class_="aw-definition")]

# Save definitions to a new file, one per line
definitions_file_path = 'anki-definitions.txt'
with open(definitions_file_path, 'w', encoding='utf-8') as file:
    file.write('\n'.join(definitions))
