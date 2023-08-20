import { useEffect } from 'react'
import { Container, Table } from 'react-bootstrap'

function Results({ searchResults }) {

  useEffect(() => {
    console.log(searchResults)
  }, [searchResults])

  const renderSearchResults = () => {
    return searchResults.map((result, index) => {
        const name = result.case_name
        const link = result.link
        const date = result.date
      return (
        <tr key={index} className='shadow-sm'>
          <td>{name}</td>
          <td>{date}</td>
          <td>{link}</td>
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
            <th>Date</th>
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