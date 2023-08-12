import { useState, useEffect } from 'react';
import axios from 'axios';

import { Container, Form, Button } from 'react-bootstrap';

const Search = () => {

  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  const handleSearch = async (e) => {
    e.preventDefault();
    console.log(`Search term: ${searchTerm}`);
    console.log(`Clicked`)

    try {
      const res = await axios.get(`/api/search/${searchTerm}`)
      const data = res.data;
      const results = data.search_results;
      setSearchResults([results]);
    } catch (err) {
      console.log(err);
    }
    setSearchTerm("");
  }

  useEffect(() => {
    console.log(`Search results: ${searchResults}`);
  }, [searchResults])
  

    return (
        <Container>
          <Form className='d-flex' onSubmit={handleSearch}>
            <Form.Control
              type='search'
              placeholder='Search Hearing Examiner decisions by keyword...'
              className='searchbar me-2 shadow-sm'
              aria-label='Search'
              onChange={(e) => setSearchTerm(e.target.value)}
              value = {searchTerm}
            >
            </Form.Control>
            <Button 
              className='shadow-sm search-btn' 
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

