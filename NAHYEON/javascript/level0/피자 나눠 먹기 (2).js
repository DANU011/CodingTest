function solution(n) {
  let pizza = 6;
  // 같은 수로 나눠질 때까지 +6
  while (pizza % n !== 0) {
      pizza += 6;
  }
  // 박스 수 반환
  return pizza / 6;
}