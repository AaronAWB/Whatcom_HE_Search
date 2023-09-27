import { useState } from 'react';
import Search from '@/components/search';
import Results from '@/components/results'

interface SearchResult {
  case_name: string;
  link: string;
  hearing_date: string;
  decision_date: string;
  hearing_examiner: string;
}

function App() {

  const [searchResults, setSearchResults] = useState<SearchResult[]>([]);
  const [hasSearched, setHasSearched] = useState<boolean>(false);

  return (
    <>
      <Search setSearchResults={setSearchResults} setHasSearched={setHasSearched} />
      <Results searchResults={searchResults} hasSearched={hasSearched} />
    </>
  )
}

export default App
