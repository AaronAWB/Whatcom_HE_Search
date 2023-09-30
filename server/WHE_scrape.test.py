import unittest
from server.application import app
from src.lib.WHE_scrape import whe_scrape

class TestWHE_Scrape(unittest.TestCase):
    
  def setUp(self):
      self.app = app.test_client()

#   def test_retrieve_pdf_data(self):
#       pdf_links = whe_scrape.retrieve_pdf_data()
#       self.assertTrue(len(pdf_links) > 0)

#   def test_extract_text(self):
#       link = 'Archive.aspx?ADID=15523'
#       extracted_text = whe_scrape.extract_text(link)
#       self.assertTrue(len(extracted_text) > 0)

  # -- Tests for date extraction edge cases --

  def test_extract_date(self):
    link = 'Archive.aspx?ADID=15523'
    extracted_text = whe_scrape.extract_text(link)
    date = whe_scrape.extract_date(extracted_text)
    self.assertTrue(len(date) > 0)

  def test_valid_hearing_date(self):
    date = 'Hearing Date 8/31/2023'
    result = whe_scrape.extract_date(date)
    self.assertEqual(result['hearingDate'], 'August 31, 2023')

  def test_valid_decision_date(self):
    date = 'Decision Date 12/15/2022'
    result = whe_scrape.extract_date(date)
    self.assertEqual(result['decisionDate'], 'December 15, 2022')

  def test_valid_decision_year(self):
    date = '2021'
    result = whe_scrape.extract_date(date)
    self.assertEqual(result['decisionDate'], '2021')

  def test_missing_hearing_date(self):
    date = 'Decision Date 5/1/2023'
    result = whe_scrape.extract_date(date)
    self.assertEqual(result['hearingDate'], 'Not listed.')

  def test_missing_decision_date(self):
    date = '2023'
    result = whe_scrape.extract_date(date)
    self.assertEqual(result['decisionDate'], '2023')

  def test_missing_decision_year(self):
    date = 'Some other text'
    result = whe_scrape.extract_date(date)
    self.assertEqual(result['decisionDate'], 'Not listed.')

  # -- Tests for date formatting edge cases --

  def test_format_date(self):
    date = '8.31.23'
    formatted_date = whe_scrape.format_date(date)
    self.assertTrue(len(formatted_date) > 0)

  def test_format_date_valid_slash_format(self):
    date = '08/31/23'
    formatted_date = whe_scrape.format_date(date)
    self.assertEqual(formatted_date, 'August 31, 2023')

  def test_format_date_valid_dot_format(self):
    date = '8.31.23'
    formatted_date = whe_scrape.format_date(date)
    self.assertEqual(formatted_date, 'August 31, 2023')

  def test_format_date_full_year(self):
    date = '8.31.2023'
    formatted_date = whe_scrape.format_date(date)
    self.assertEqual(formatted_date, 'August 31, 2023')

  def test_format_date_invalid_format(self):
    date = 'Some invalid date'
    formatted_date = whe_scrape.format_date(date)
    self.assertEqual(formatted_date, date)

  def test_format_date_empty_input(self):
    date = ''
    formatted_date = whe_scrape.format_date(date)
    self.assertEqual(formatted_date, date)

#   def test_search_keyword(self):
#     keyword = 'wedding'
#     search_results = whe_scrape.search_keyword(keyword)
#     self.assertTrue(len(search_results) > 0)

  def test_get_metadata(self):
    metadata = whe_scrape.get_metadata()
    self.assertTrue(len(metadata) > 0)

if __name__ == '__main__':
    unittest.main()