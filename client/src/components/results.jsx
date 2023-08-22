import { Container, Table } from 'react-bootstrap'
import '@Styles/results.css'

function Results({ searchResults }) {

  const renderSearchResults = () => {
    return searchResults.map((result, index) => {
        const name = result.case_name
        const link = result.link
        const hearingDate = result.hearing_date
        const decisionFullDate = result.decision_full_date
        const decisionYearOnly = result.decision_year_only
        const decisionDate = decisionFullDate ? decisionFullDate : decisionYearOnly;
        const hearingExaminer = result.hearing_examiner
        
      return (
        <tr key={index} className='shadow-sm'>
          <td>{name}</td>
          <td className={hearingExaminer === 'Unable to locate.' ? 'unable-to-locate' : ''}>{hearingExaminer}</td>
          <td className={hearingDate === 'Not listed.' ? 'not-listed' : ''}>{hearingDate}</td>
          <td className={decisionDate === 'Not listed.' ? 'not-listed' : ''}>{decisionDate}</td>
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
            <th>Hearing Examiner</th>
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