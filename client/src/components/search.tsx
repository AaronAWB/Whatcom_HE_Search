import { useState } from 'react';
import axios from 'axios';

import { Container, Form, Row, Col, Button } from 'react-bootstrap';

import '@Styles/Search.css';

interface SearchProps {
  setSearchResults: (results: any[]) => void;
}

const Search = ({ setSearchResults }: SearchProps) => {

  const [searchParameters, setSearchParameters] = useState<{
    keyword: string;
    examiner: string;
    hearingDate: string;
    decisionDate: string;
  }>({
    keyword: '',
    examiner: '',
    hearingDate: '',
    decisionDate: '',
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
  }

    return (

      <Container className='shadow-sm search-container mt-5'>
        <Form onSubmit={handleSearch}>
          <Row className='mb-3 mt-3'>
            <Form.Group as={Col} md='6' className='mt-2'>
              <Form.Label>Keyword:</Form.Label>
              <Form.Control
                name='keyword' 
                type='text' 
                placeholder='Filter decisions by keyword...' 
                value={searchParameters.keyword}
                onChange={handleInputChange}
                />
            </Form.Group>
            <Form.Group as={Col} md='6' className='mt-2'>
              <Form.Label>Hearing Examiner:</Form.Label>
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
              <Form.Label>Hearing Date:</Form.Label>
              <Form.Control
                name='hearingDate' 
                type='date' 
                value={searchParameters.hearingDate}
                onChange={handleInputChange} 
                />
            </Form.Group>
            <Form.Group as={Col} md='6'>
              <Form.Label>Decision Date:</Form.Label>
              <Form.Control 
                name='decisionDate'
                type='date' 
                value={searchParameters.decisionDate}
                onChange={handleInputChange}  
                />
            </Form.Group>
          </Row>
          <Button 
              className='shadow-sm search-btn mb-3 mt-2' 
              variant='primary' 
              type='submit'
              >
              Search
          </Button>
        </Form>
      </Container>
    )
}

export default Search;

