function solution(myString) {
  let lower = myString.toLowerCase();
  let answer = lower.replaceAll('a','A');       
  return answer;
}