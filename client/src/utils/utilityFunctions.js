
const formatDate = (date) => {

  const isValidFormat = /^\d{1,2}\.\d{1,2}\.\d{4}$/.test(date);

  if (isValidFormat) {
    const months = [
      'January', 'February', 'March', 'April', 'May', 
      'June', 'July', 'August', 'September', 'October', 
      'November','December'
    ]
  
    const dateSections = date.split('.')
    const monthIndex = months[parseInt(dateSections[0]) - 1]
    const day = dateSections[1]
    const year = dateSections[2]
  
    const formattedDate = `${monthIndex} ${day}, ${year}`
  
    return formattedDate

  }

  return date
}

export { formatDate }