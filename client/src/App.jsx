import { useState } from 'react';
import Search from './components/Search';
import Results from './components/Results';

function App() {

  const [searchResults, setSearchResults] = useState([]);
  

  return (
    <>
      <Search setSearchResults={setSearchResults} />
      <Results searchResults={searchResults} />
    </>
  )
}

export default App
