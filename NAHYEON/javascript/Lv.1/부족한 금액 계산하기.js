function solution(price, money, count) {
  let totalPrice = 0;
  let answer = 0;
  for (let i = 1; i <= count; i++) {
      totalPrice = price * i + totalPrice;
  }
  if (money < totalPrice) {
      answer = totalPrice - money;
  }
  else {
      answer = 0;
  }
  return answer;
}