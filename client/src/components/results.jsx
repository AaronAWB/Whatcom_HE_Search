import { Container, Table } from 'react-bootstrap'

function Results({ searchResults }) {

  const extractDates = date => {
    const hearingDatePattern = /(\d{1,2}\/\d{1,2}\/\d{4})/;
    const decisionDatePattern = /(\d{1,2}\/\d{1,2}\/\d{4})/;

    const hearingDateMatch = date.match(hearingDatePattern);
    const decisionDateMatch = date.match(decisionDatePattern);

    const hearingDate = hearingDateMatch ? hearingDateMatch[1] : null;
    const decisionDate = decisionDateMatch ? decisionDateMatch[1] : null;

    return { hearingDate, decisionDate };
  }

  const renderSearchResults = () => {
    return searchResults.map((result, index) => {
        const name = result.case_name
        const link = result.link
        const {hearingDate, decisionDate} = extractDates(result.date);
      return (
        <tr key={index} className='shadow-sm'>
          <td>{name}</td>
          <td>{hearingDate}</td>
          <td>{decisionDate}</td>
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