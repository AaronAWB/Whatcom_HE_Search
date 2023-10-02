import unittest
from server.application import app
from server.src.lib.data_extraction import data_extraction

class Testdata_extraction(unittest.TestCase):
    
  def setUp(self):
      self.app = app.test_client()

  # -- Tests for date extraction edge cases --

  def test_extract_date(self):
    link = 'Archive.aspx?ADID=15523'
    extracted_text = data_extraction.extract_text(link)
    date = data_extraction.extract_date(extracted_text)
    self.assertTrue(len(date) > 0)

  def test_valid_hearing_date(self):
    date = 'Hearing Date 8/31/2023'
    result = data_extraction.extract_date(date)
    self.assertEqual(result['hearingDate'], 'August 31, 2023')

  def test_valid_decision_date(self):
    date = 'Decision Date 12/15/2022'
    result = data_extraction.extract_date(date)
    self.assertEqual(result['decisionDate'], 'December 15, 2022')

  def test_valid_decision_year(self):
    date = '2021'
    result = data_extraction.extract_date(date)
    self.assertEqual(result['decisionDate'], '2021')

  def test_missing_hearing_date(self):
    date = 'Decision Date 5/1/2023'
    result = data_extraction.extract_date(date)
    self.assertEqual(result['hearingDate'], 'Not listed.')

  def test_missing_decision_date(self):
    date = '2023'
    result = data_extraction.extract_date(date)
    self.assertEqual(result['decisionDate'], '2023')

  def test_missing_decision_year(self):
    date = 'Some other text'
    result = data_extraction.extract_date(date)
    self.assertEqual(result['decisionDate'], 'Not listed.')

  # -- Tests for date formatting edge cases --

  def test_format_date(self):
    date = '8.31.23'
    formatted_date = data_extraction.format_date(date)
    self.assertTrue(len(formatted_date) > 0)

  def test_format_date_valid_slash_format(self):
    date = '08/31/23'
    formatted_date = data_extraction.format_date(date)
    self.assertEqual(formatted_date, 'August 31, 2023')

  def test_format_date_valid_dot_format(self):
    date = '8.31.23'
    formatted_date = data_extraction.format_date(date)
    self.assertEqual(formatted_date, 'August 31, 2023')

  def test_format_date_full_year(self):
    date = '8.31.2023'
    formatted_date = data_extraction.format_date(date)
    self.assertEqual(formatted_date, 'August 31, 2023')

  def test_format_date_invalid_format(self):
    date = 'Some invalid date'
    formatted_date = data_extraction.format_date(date)
    self.assertEqual(formatted_date, date)

  def test_format_date_empty_input(self):
    date = ''
    formatted_date = data_extraction.format_date(date)
    self.assertEqual(formatted_date, date)

  def test_get_metadata(self):
    metadata = data_extraction.get_metadata()
    self.assertTrue(len(metadata) > 0)

if __name__ == '__main__':
    unittest.main()