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
    # Finds all <a> tags in the html and extracts the links
    for link in soup.find_all('a'):
        links = link.get('href')
        if links is not None:
            link_list = links.split()
            
            # Adds all links starting with 'Archive.aspx?ADID' to pdf_links
            pdf_links.extend([pdf_link for pdf_link in link_list if pdf_link.startswith('Archive.aspx?ADID')])
    
def search_keyword(pdf_links, keyword):
    
    base_url = "https://wa-whatcomcounty.civicplus.com/"
    retrieve_pdf_links()
    search_results = []
    
    for link in pdf_links:
        complete_link = urllib.parse.urljoin(base_url, link)
        response = requests.get(complete_link)
        pdf_content = response.content
        # get_metadata(pdf_content)

        # Creates a PyPDF2 reader object to read the PDF content
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_content))
        
        # Checks if the PDF has a valid /Root object
        # if '/Root' not in pdf_reader.trailer:
        #     print(f"Invalid PDF: {link}")
        #     continue
        
        # Extracts the text from the PDF using pdfminer, deletes whitespace, and checks if the keyword is in the text
        text = extract_text(BytesIO(pdf_content)).strip()
        if keyword in text:
            search_results.append(link)

        # Checks if the PDF is text-based, if not, runs OCR on the PDF            
        # if not text.strip():
        #     print(f"PDF is not text-based: {link}. Running OCR...")
        #     image_to_text(pdf_content, keyword, link)

    return search_results

def get_metadata(pdf_content):

    try:
        # Creates a PyPDF2 reader object to extract the metadata
        pdf_stream = BytesIO(pdf_content)
        pdf_reader = PyPDF2.PdfReader(pdf_stream)
        metadata = pdf_reader.metadata
        print(metadata)

    except:
        print("No metadata found")

# def image_to_text(pdf_content, keyword, link):
#     pdf_stream = BytesIO(pdf_content)
#     pdf_reader = PyPDF2.PdfReader(pdf_stream)

#     for page in pdf_reader.pages:
#         resources = page['/Resources']
#         if resources is not None and '/XObject' in resources:
#             xobjects = resources['/XObject']
#             for obj in xobjects.values():
#                 if isinstance(obj, PyPDF2.generic.IndirectObject):
#                     obj = obj.resolve()

#                 if obj['/Subtype'] == '/Image':
#                     image_stream = obj._data
#                     image = Image.open(BytesIO(image_stream))
#                     extracted_text = pytesseract.image_to_string(image)

#                     if keyword in extracted_text:
#                         print(f"Keyword '{keyword}' found in image from PDF: {link}")
#                     else:
#                         print(f"Keyword '{keyword}' not found in scanned PDF: {link}")
#     else:
#         print(f"No valid images found in PDF: {link}")

search_results = search_keyword(pdf_links, 'Rajeev')

for result in search_results:
    print(result)
