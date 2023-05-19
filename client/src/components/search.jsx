// import { useState } from 'react';
import axios from 'axios';

const Search = () => {

  const URL = "https://wa-whatcomcounty.civicplus.com/Archive.aspx?AMID=43";

  // const [searchTerm, setSearchTerm] = useState("");
  // const [searchResults, setSearchResults] = useState([]);

  const handleFormSubmit = async (e) => {
    e.preventDefault();
    console.log('Button clicked');
    try {
      const res = await axios.get(URL);
      const htmlContent = res.data;
      const pdfLinks = parseHtml(htmlContent);
      processPDFS(pdfLinks);
    } catch (error) {
      console.log('Error parsing webpage:', error);
    }
  }

  const parseHtml = (htmlContent) => {
    const parser = new DOMParser();
    const doc = parser.parseFromString(htmlContent, 'text/html');
    const pdfLinks = Array.from(doc.querySelectorAll('a[href]')).reduce(
      (links, link) => {
        const href = link.getAttribute('href');
        if (href.toLowerCase().endsWith('.pdf')) {
          links.push(href);
        }
        return links;
      },[]);
    console.log(pdfLinks);
    return pdfLinks;
  };
  

    return (
        <>
          <button onClick={handleFormSubmit}>Test Button</button> 
        </>
    )
}

export default Search;

