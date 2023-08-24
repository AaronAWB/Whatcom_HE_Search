import { useState, useEffect } from 'react';
import Search from './components/Search';
import Results from './components/Results';

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
