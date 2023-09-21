import os
import requests
import ocrmypdf
from PyPDF2 import PdfReader

def convert_unsearchable_pdf(link):
        try:
            base_url = "https://wa-whatcomcounty.civicplus.com/"
            complete_link = base_url + link
            response = requests.get(complete_link)

            directory = "/tmp"
            os.makedirs(directory, exist_ok=True)

            input_file = os.path.join(directory, 'input.pdf')
            output_file = os.path.join(directory, 'output.pdf')
            
            if response.status_code == 200:
                with open('input.pdf', 'wb') as f:
                    f.write(response.content)
            else:
                print(f"Failed to retrieve PDF, status code: {response.status_code}")

            input_file = 'input.pdf'
            output_file = 'output.pdf'

            ocrmypdf.ocr(input_file, output_file, force_ocr=True)

            with open(output_file, 'rb') as f:
                reader = PdfReader(f)
                extracted_text=""
                for page_num in range (len(reader.pages)):
                    page = reader.pages[page_num]
                    extracted_text += page.extract_text()
            
            os.remove(input_file)
            os.remove(output_file)
    
            print(extracted_text)
            return extracted_text
              
        except Exception as e:
            print(f"Error converting PDF: {e}")
            return f"Error converting non-searchable PDF{link}"
        
convert_unsearchable_pdf('Archive.aspx?ADID=15497')