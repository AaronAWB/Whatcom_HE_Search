import requests
import urllib.parse
from bs4 import BeautifulSoup
from io import BytesIO
from pdfminer.high_level import extract_text
from pdfminer.pdfparser import PDFSyntaxError

URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43";
html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'html.parser')

pdf_links = []

def retrieve_pdf_links():
    for link in soup.find_all('a'):
        links = link.get('href')
        if links is not None:
            link_list = links.split()
            pdf_links.extend([pdf_link for pdf_link in link_list if pdf_link.startswith('Archive')])

def search_keyword_in_pdfs(pdf_links, keyword):
    
    base_url = "https://wa-whatcomcounty.civicplus.com/"
    retrieve_pdf_links()

    for link in pdf_links:
        complete_link = urllib.parse.urljoin(base_url, link)
        response = requests.get(complete_link)
        pdf_content = response.content

        try:
            text = extract_text(BytesIO(pdf_content))
            if keyword in text:
                print(f"Keyword '{keyword}' found in PDF: {link}")
        except PDFSyntaxError as e:
            if "/Root object" in str(e):
                print(f"Invalid PDF: {link} (Missing /Root object)")

search_keyword_in_pdfs(pdf_links, 'Rajeev')