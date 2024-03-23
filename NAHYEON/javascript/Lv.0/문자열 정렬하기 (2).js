function solution(my_string) {
  let answer = my_string.toLowerCase()
  return answer.split('').sort().join('')
}