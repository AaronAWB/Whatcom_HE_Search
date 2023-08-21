import { Container, Table } from 'react-bootstrap'

function Results({ searchResults }) {

  const extractDates = date => {
    const hearingDatePattern = /Hearing Date (\d{1,2}\/\d{1,2}\/\d{4})/;
    const decisionDatePattern = /Decision Date (\d{1,2}\/\d{1,2}\/\d{4})/;
    const decisionYearPattern = /(\d{4})/;

    const hearingDateMatch = date.match(hearingDatePattern);
    const decisionDateMatch = date.match(decisionDatePattern);
    const decisionYearMatch = date.match(decisionYearPattern);

    const hearingDate = hearingDateMatch ? hearingDateMatch[1] : 'Not listed.';
    const decisionDate = decisionDateMatch ? decisionDateMatch[1] : 'Not listed.';
    const decisionYear = decisionYearMatch ? decisionYearMatch[1] : 'Not listed.';

    return { hearingDate, decisionDate, decisionYear };
  }

  const renderSearchResults = () => {
    return searchResults.map((result, index) => {
        const name = result.case_name
        const link = result.link
        const {hearingDate, decisionDate, decisionYear} = extractDates(result.date);
        const decisionDateDisplay = decisionDate ? decisionDate : decisionYear;
      return (
        <tr key={index} className='shadow-sm'>
          <td>{name}</td>
          <td>{hearingDate}</td>
          <td>{decisionDateDisplay}</td>
          <td>
            <a href={'https://wa-whatcomcounty.civicplus.com/' + link} >
              PDF
            </a>
          </td>
        </tr>
      )
    })
  }

  return(
    <Container className='mt-5'>
      <Table striped hover className='shadow-sm'>
        <thead>
          <tr>
            <th>Case Name</th>
            <th>Hearing Date</th>
            <th>Decision Date</th>
            <th>Link</th>
          </tr>
        </thead>
        <tbody>
          {renderSearchResults()}
        </tbody>
      </Table>
    </Container>
  )
}

export default Results