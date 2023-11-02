function solution(my_string, n) {
  let array = [...my_string];
  let answer = [];
  for (let i = 0; i < n; i++) {
      answer.push(array[i]);
  }
  return answer.join('');
}