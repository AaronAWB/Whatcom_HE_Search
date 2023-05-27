import requests
from bs4 import BeautifulSoup

URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43";
html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'html.parser')