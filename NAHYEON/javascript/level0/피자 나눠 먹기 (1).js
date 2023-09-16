function solution(n) {
  var answer = 0;
  if ( n % 7 == 0) {
      answer = n / 7;
  }
  else if ( n == 1) {
      answer = 1;
  }
  else {
      answer = Math.floor(n / 7) + 1;
  }
  return answer;
}

// Math.floor 주어진 숫자와 같거나 작은 정수 중에서 가장 큰 수를 반환
// Math.floor(5.95) -> 5, Math.floor(-5.05) -> -6
// Math.ceil 주어진 숫자보다 크거나 같은 숫자 중 가장 작은 숫자를 integer 로 반환
// Math.ceil(7.004)-> 8, Math.ceil(-7.004) -> 7
// parseInt 문자열 인자를 파싱하여 특정 진수의 정수를 반환