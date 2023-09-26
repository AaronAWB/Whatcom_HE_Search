import { useState } from 'react';
import axios from 'axios';

import { Container, Form, Row, Col, Button } from 'react-bootstrap';

import '@Styles/Search.css';

interface SearchProps {
  setSearchResults: (results: any[]) => void;
}


const Search = ({ setSearchResults }: SearchProps) => {

  const [keyword, setKeyword] = useState<string>("");
  const [hearingExaminer, setHearingExaminer] = useState<string>("");
  const [hearingDate, setHearingDate] = useState<string>("");
  const [decisionDate, setDecisionDate] = useState<string>("");
  const [displayedTerm, setDisplayedTerm] = useState<string>("");

  const handleSearch = async (e: any) => {
    e.preventDefault();
    setDisplayedTerm(searchTerm);

    try {
      const res = await axios.get(`/api/search/${searchTerm}`)
      const data = res.data;
      const results = data.search_results;
      setSearchResults(results);
    } catch (err) {
      console.log(err);
    }
    setSearchTerm("");
  }

    return (

      <Container className='shadow-sm'>
        <Form>
          <Row className='mb-3 mt-3'>
            <Form.Group as={Col} md='6'>
              <Form.Label>Keyword:</Form.Label>
              <Form.Control type='text' placeholder='Filter decisions by keyword...' className='shadow-sm' />
            </Form.Group>
            <Form.Group as={Col} md='6'>
              <Form.Label>Hearing Examiner:</Form.Label>
              <Form.Control type='text' placeholder='Filter decisions by Hearing Examiner...' className='shadow-sm' />
            </Form.Group>
          </Row>
          <Row className='mb-3'>
            <Form.Group as={Col} md='6'>
              <Form.Label>Hearing Date:</Form.Label>
              <Form.Control type='date' placeholder='Filter decisions by hearing date...' className='shadow-sm' />
            </Form.Group>
            <Form.Group as={Col} md='6'>
              <Form.Label>Decision Date:</Form.Label>
              <Form.Control type='date' placeholder='Filter decisions by decision date...' className='shadow-sm' />
            </Form.Group>
          </Row>
          <Button 
              className='shadow-sm search-btn' 
              variant='primary' 
              type='submit'
              >
              Search
          </Button>
        </Form>
        <Container className='mt-3 displayed-term-container'>
          <span className={`displayed-term-text ${displayedTerm ? 'visible-text' : 'hidden-text'}`}>
            The following decisions contain the keyword: {`"${displayedTerm}"`}
          </span>
        </Container>
      </Container>







        // <Container className='show-sm mt-5'>
        //   <Form className='d-flex' onSubmit={handleSearch}>
        //     <Form.Control
        //       type='search'
        //       placeholder='Search Hearing Examiner decisions by keyword...'
        //       className='searchbar me-2 shadow-sm'
        //       aria-label='Search'
        //       onChange={(e) => setSearchTerm(e.target.value)}
        //       value = {searchTerm}
        //     >
        //     </Form.Control>
        //     <Button 
        //       className='shadow-sm search-btn' 
        //       variant='primary' 
        //       type='submit'
        //       >
        //       Search
        //     </Button>
        //   </Form>
        //     <Container className='mt-3 displayed-term-container'>
        //       <span className={`displayed-term-text ${displayedTerm ? 'visible-text' : 'hidden-text'}`}>
        //         The following decisions contain the keyword: {`"${displayedTerm}"`}
        //       </span>
        //     </Container>
        // </Container>
    )
}

export default Search;

