function solution(box, n) {
  var answer = 1;
  for (v of box) answer *= Math.floor(v / n);
  return answer;
}