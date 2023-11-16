function solution(n) {
  let arr = String(n).split('').map(Number);
  let desc = arr.sort(function(a, b){return b-a});
  let answer = desc.join('');
  return Number(answer);
}