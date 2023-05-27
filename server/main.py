import requests
from bs4 import BeautifulSoup

URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43";
html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'html.parser')

pdf_links = []

for link in soup.find_all('a'):
    links = link.get('href')
    if links is not None:
        link_list = links.split()
        pdf_links.extend([pdf_link for pdf_link in link_list if pdf_link.startswith('Archive')])

print(f'The PDF links are: {pdf_links}')