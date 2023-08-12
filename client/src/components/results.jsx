import { Container, Table } from 'react-bootstrap'

function Results({ searchResults }) {

  const renderSearchResults = () => {
    return searchResults.map((result, index) => {
      return (
        <tr key={index}>
          <td>{result}</td>
        </tr>
      )
    })
  }

  return(
    <Container className='mt-5'>
      <Table bordered hover>
        <thead>
          <tr>
            <th>Link Id</th>
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