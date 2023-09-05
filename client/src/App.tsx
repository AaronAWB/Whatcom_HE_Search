import { useState, useEffect } from 'react';
import Search from '@/components/search';
import Results from '@/components/results'

function App() {

  const [searchResults, setSearchResults] = useState([]);

  useEffect(() => {
    console.log('searchResults: ', searchResults);
  }, [searchResults]);
  

  return (
    <>
      <Search setSearchResults={setSearchResults} />
      <Results searchResults={searchResults} />
    </>
  )
}

export default App
