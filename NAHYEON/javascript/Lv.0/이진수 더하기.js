function solution(bin1, bin2) {
  return (parseInt(bin1, 2) + parseInt(bin2, 2)).toString(2);
}

// parseInt() -> 문자열을 파싱 하여 특정 진수의 정수를 반환 (= 특정 진수를 10진수로)
// toString() -> 숫자의 경우 선택적으로 기수(2~36)를 매개변수로 취하며, 이를 통해 10진수를 특정 진수로 변환한 값 반환