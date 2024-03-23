function solution(rny_string) {
  // 정규표현식
  var answer = rny_string.replace(/m/g, 'rn');
  return answer;
}