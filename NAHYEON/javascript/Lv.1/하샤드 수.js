function solution(x) {
  var answer = '';
  let plus = 0;
  const arr = String(x).split('').map(Number);
  for(let i = 0; i < arr.length; i++) {
      plus = plus + arr[i];
  }
  if (x % plus === 0) {
      answer = true;
  }
  else answer = false;
  return answer;
}