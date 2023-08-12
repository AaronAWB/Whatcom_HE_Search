import requests
import urllib.parse
import PyPDF2

from bs4 import BeautifulSoup
from io import BytesIO
from pdfminer.high_level import extract_text


class WHE_Scrape:

    def __init__(self):
        self.URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43"
        self.html = requests.get(self.URL).text
        self.soup = BeautifulSoup(self.html, 'html.parser')
        self.pdf_links = []

    def retrieve_pdf_links(self):
        # Finds all <a> tags in the html and extracts the links
        for link in self.soup.find_all('a'):
            links = link.get('href')
            if links is not None:
                link_list = links.split()

                # Adds all links starting with 'Archive.aspx?ADID' to pdf_links
                self.pdf_links.extend([pdf_link for pdf_link in link_list if pdf_link.startswith('Archive.aspx?ADID')])

    def search_keyword(self, keyword):
            
            base_url = "https://wa-whatcomcounty.civicplus.com/"
            self.retrieve_pdf_links()
            search_results = []
    
            for link in self.pdf_links:
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

                for result in search_results:
                    print(result)
    
            return search_results
    
    def get_metadata(self, pdf_content):
        
            try:
                # Creates a PyPDF2 reader object to extract the metadata
                pdf_reader = PyPDF2.PdfFileReader(BytesIO(pdf_content))
                metadata = pdf_reader.getDocumentInfo()
                print(metadata)
            except:
                print("No metadata found.")

    

whe_scrape = WHE_Scrape()