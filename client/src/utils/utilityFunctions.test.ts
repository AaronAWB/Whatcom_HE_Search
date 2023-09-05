import { expect, test } from 'vitest'
import { formatDate } from '@/utils/utilityFunctions'

test('formats a date from MM.DD.YYYY to Month DD, YYYY', () => {
  const date = '8.25.2023'
  const formattedDate = formatDate(date)
  expect(formattedDate).toBe('August 25, 2023')
})

test('returns the date if it is not in the correct format', () => {
  const date = 'August 25, 2023'
  const formattedDate = formatDate(date)
  expect(formattedDate).toBe(date)
})