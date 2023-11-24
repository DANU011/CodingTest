function solution(s) {
  var answer = '';
  let number = Math.floor(s.length / 2);
  if (s.length % 2 !== 0){
      answer = s.charAt(number);
  }
  else {
      answer = s.substring(number-1, number+1);
  }
  return answer;
}