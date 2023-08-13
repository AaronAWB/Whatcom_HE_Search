import requests
import urllib.parse
from PyPDF2 import PdfReader

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
                complete_link = base_url + link
                response = requests.get(complete_link)
                pdf_content = response.content
 
                # Extracts the text from the PDF using pdfminer and checks if the keyword is in the text
                text = extract_text(BytesIO(pdf_content))
                if keyword in text:
                    search_results.append(link)
    
                # Checks if the PDF is text-based, if not, runs OCR on the PDF
                # if not text.strip():
                #     print(f"PDF is not text-based: {link}. Running OCR...")
                #     image_to_text(pdf_content, keyword, link)

                for result in search_results:
                    print(result)
    
            return search_results
    
    def get_metadata(self):
            
            base_url = "https://wa-whatcomcounty.civicplus.com/"
            
            try:
                # Creates a PyPDF2 reader object to extract the metadata
                link = 'Archive.aspx?ADID=15523'
                complete_link = base_url + link
                response = requests.get(complete_link)
                pdf_content = response.content

                pdf_reader = PdfReader(BytesIO(pdf_content))
                metadata = pdf_reader.metadata
                return metadata
            except:
                print("No metadata found.")

    

whe_scrape = WHE_Scrape()