import requests
import urllib.parse
import pytesseract
import PyPDF2

from bs4 import BeautifulSoup
from io import BytesIO
from pdfminer.high_level import extract_text
from pdfminer.pdfdocument import PDFTextExtractionNotAllowed
from PIL import Image
from pdf2image import convert_from_bytes


URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43";
html_text = requests.get(URL).text

soup = BeautifulSoup(html_text, 'html.parser')

pdf_links = ['Archive.aspx?ADID=14932']

# def retrieve_pdf_links():
#     for link in soup.find_all('a'):
#         links = link.get('href')
#         if links is not None:
#             link_list = links.split()
#             pdf_links.extend([pdf_link for pdf_link in link_list if pdf_link.startswith('Archive')])
    
def search_keyword_in_pdfs(pdf_links, keyword):
    
    base_url = "https://wa-whatcomcounty.civicplus.com/"
    
    for link in pdf_links:
        complete_link = urllib.parse.urljoin(base_url, link)
        response = requests.get(complete_link)
        pdf_content = response.content

        try:
            pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_content))
            if '/Root' not in pdf_reader.trailer:
                print(f"Invalid PDF: {link}")
                continue

            try:
                text = extract_text(BytesIO(pdf_content)).strip()
                print(f"Here is the text of the PDF: {text}")
                if keyword in text:
                    print(f"Keyword '{keyword}' found in PDF: {link}")
                    print("Text Format: Searchable Text")
                else:
                    print(f"Keyword '{keyword}' not found in PDF: {link}")
                    print("Text Format: Searchable Text")
            except PDFTextExtractionNotAllowed:
                print(f"Text extraction not allowed in PDF: {link}")
                print("Text Format: Image")

            if not text.strip():
                print(f"PDF is not text-based: {link}")
                print("Text Format: Image")
                print("Running OCR...")
                
                has_image = False
                images = convert_from_bytes(pdf_content)
                for i, image in enumerate(images):
                    image_path = f"image_{i}.png"
                    image.save(image_path)
                    extracted_text = pytesseract.image_to_string(Image.open(image_path)).strip()
                    if keyword in extracted_text:
                        print(f"Keyword '{keyword}' found in image from PDF: {link}")
                        has_image = True

                if not has_image:
                    print(f"No image found in PDF: {link}")

        except Exception:
            print(f"Invalid PDF: {link}")


search_keyword_in_pdfs(pdf_links, 'Michael')