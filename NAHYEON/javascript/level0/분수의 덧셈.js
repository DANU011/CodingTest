function solution(numer1, denom1, numer2, denom2) {
  // 분자
  let topNum = numer1 * denom2 + numer2 * denom1;
  // 분모
  let botNum = denom1 * denom2;
  // 최대 공약수
  let maximum = 1;
  // 약분
  for (let i = 1 ; i <= topNum ; i++ ) {
      if (topNum % i === 0 && botNum % i === 0){
          maximum = i
      }
  }
  return [topNum/maximum, botNum/maximum];
}