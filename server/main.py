import requests
import urllib.parse
import pytesseract
import PyPDF2

from bs4 import BeautifulSoup
from io import BytesIO
from pdfminer.high_level import extract_text
from PIL import Image

URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43"
html = requests.get(URL).text

soup = BeautifulSoup(html, 'html.parser')

pdf_links = []


def retrieve_pdf_links():
    for link in soup.find_all('a'):
        links = link.get('href')
        if links is not None:
            link_list = links.split()
            pdf_links.extend([pdf_link for pdf_link in link_list if pdf_link.startswith('Archive.aspx?ADID')])


def search_keyword(pdf_links, keyword):

    base_url = "https://wa-whatcomcounty.civicplus.com/"
    retrieve_pdf_links()
    print(pdf_links)

    for link in pdf_links:
        complete_link = urllib.parse.urljoin(base_url, link)
        response = requests.get(complete_link)
        pdf_content = response.content
        get_metadata(pdf_content)

        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_content))
        if '/Root' not in pdf_reader.trailer:
            print(f"Invalid PDF: {link}")
            continue

        text = extract_text(BytesIO(pdf_content)).strip()
        if keyword in text:
            print(f"Keyword '{keyword}' found in PDF: {link}")

        if not text.strip():
            print(f"PDF is not text-based: {link}. Running OCR...")
            image_to_text(pdf_content, keyword, link)


def get_metadata(pdf_content):

    try:
        pdf_stream = BytesIO(pdf_content)
        pdf_reader = PyPDF2.PdfReader(pdf_stream)
        metadata = pdf_reader.metadata
        print(metadata)

    except:
        print("No metadata found")


def image_to_text(image_data, keyword, link):
    image = Image.open(BytesIO(image_data))
    extracted_text = pytesseract.image_to_string(image)

    if keyword in extracted_text:
        print(f"Keyword '{keyword}' found in image from PDF: {link}")


search_keyword(pdf_links, 'Whatcom')
