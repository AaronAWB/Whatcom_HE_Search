import { useState } from 'react';
import axios from 'axios';

const Search = () => {

  const URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43";

  const [searchTerm, setSearchTerm] = useState("");
  const [searchResults, setSearchResults] = useState([]);

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    try {
      const res = await axios.get(URL);
      const htmlContent = res.data;
      const pdfLinks = parseHtml(htmlContent);
      processPDFS(pdfLinks);
    } catch (error) {
      console.log('Error parsing webpage:', error);
    }


  


    return (
        <>
        </>
    )
}

export default Search;

