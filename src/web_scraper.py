import requests
from bs4 import BeautifulSoup

def fetch_definition(word):
    url = f"https://www.dictionary.com/browse/{word}"
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        definition = soup.find('div', {'class': 'e1q3nk1v4'})
        if definition:
            return definition.text
    return "Definition not found."
