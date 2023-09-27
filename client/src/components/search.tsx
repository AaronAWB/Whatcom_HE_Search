import { useState } from 'react';
import axios from 'axios';

import { Container, Form, Row, Col, Button } from 'react-bootstrap';

import '@Styles/Search.css';

interface SearchProps {
  setSearchResults: (results: any[]) => void;
  setHasSearched: (hasSearched: boolean) => void;
}

const Search = ({ setSearchResults, setHasSearched }: SearchProps) => {

  const [searchParameters, setSearchParameters] = useState<{
    keyword: string;
    examiner: string;
    hearingDate: string;
    decisionDate: string;
    month: string;
    year: string;
  }>({
    keyword: '',
    examiner: '',
    hearingDate: '',
    decisionDate: '',
    month: '',
    year: ''
  });
  
  const handleInputChange = (e: any) => {
    const { name, value } = e.target;
    setSearchParameters({
      ...searchParameters,
      [name]: value,
    });
  }

  const handleSearch = async (e: any) => {
    e.preventDefault();

    const queryString = new URLSearchParams(searchParameters).toString();
    console.log(queryString);

    try {
      const res = await axios.get(`/api/search?${queryString}`)
      const data = res.data;
      const results = data.search_results;
      setSearchResults(results);
    } catch (err) {
      console.log(err);
    };
    setHasSearched(true);
  }

  const onClick = async (e: any) => {
    e.preventDefault();
    setSearchParameters({
      keyword: '',
      examiner: '',
      hearingDate: '',
      decisionDate: '',
      month: '',
      year: ''
    })
  }

    return (

      <Container className='shadow-sm search-container mt-5'>
        <div className='title-container mt-3'>
          <h3 className='title'>
            <span className='county-name'>
              Whatcom County {''}
            </span> 
            Hearing Examiner Decision Search
          </h3>
        </div>
        <Form onSubmit={handleSearch}>
          <Row className='mb-3 mt-2'>
            <Form.Group as={Col} md='6' className='mt-1'>
              <Form.Label className='form-label'>Keyword:</Form.Label>
              <Form.Control
                name='keyword' 
                type='text' 
                placeholder='Filter decisions by keyword...' 
                value={searchParameters.keyword}
                onChange={handleInputChange}
                />
            </Form.Group>
            <Form.Group as={Col} md='6' className='mt-1'>
              <Form.Label className='form-label'>Hearing Examiner:</Form.Label>
              <Form.Control 
                name='examiner'
                type='text' 
                placeholder='Filter decisions by Hearing Examiner...' 
                value={searchParameters.examiner}
                onChange={handleInputChange}
                />
            </Form.Group>
          </Row>
          <Row className='mb-3'>
            <Form.Group as={Col} md='6'>
              <Form.Label className='form-label'>Hearing Date:</Form.Label>
              <Form.Control
                name='hearingDate' 
                type='date' 
                value={searchParameters.hearingDate}
                onChange={handleInputChange} 
                />
            </Form.Group>
            <Form.Group as={Col} md='6'>
              <Form.Label className='form-label'>Decision Date:</Form.Label>
              <Form.Control 
                name='decisionDate'
                type='date' 
                value={searchParameters.decisionDate}
                onChange={handleInputChange}  
                />
            </Form.Group>
          </Row>
          <Row className='mb-3'>
            <Form.Group as={Col} md='6'>
              <Form.Label className='form-label'>Month:</Form.Label>
              <Form.Select 
                name='month'
                value={searchParameters.month}
                onChange={handleInputChange}
                >
                  <option value=''>Select Month</option>
                  <option value='January'>January</option>
                  <option value='February'>February</option>
                  <option value='March'>March</option>
                  <option value='April'>April</option>
                  <option value='May'>May</option>
                  <option value='June'>June</option>
                  <option value='July'>July</option>
                  <option value='August'>August</option>
                  <option value='September'>September</option>
                  <option value='October'>October</option>
                  <option value='November'>November</option>
                  <option value='December'>December</option>
              </Form.Select>
</Form.Group>
            <Form.Group as={Col} md='6'>
              <Form.Label className='form-label'>Year:</Form.Label>
              <Form.Control 
                name='year'
                type='text' 
                value={searchParameters.year}
                onChange={handleInputChange}  
                />
            </Form.Group>
          </Row>
          <Row>
            <Form.Group as={Col} md='6'>
              <Button 
                  className='shadow-sm search-btn mb-3 mt-2' 
                  variant='primary' 
                  type='submit'
                  >
                  Search
              </Button>
            </Form.Group> 
            <Form.Group as={Col} md='6'>
              <Button 
                  className='shadow-sm clear-btn mb-3 mt-2' 
                  variant='primary' 
                  onClick={onClick}
                  >
                  Clear
              </Button>
            </Form.Group>
          </Row> 
        </Form>
      </Container>
    )
}

export default Search;

