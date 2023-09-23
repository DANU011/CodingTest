function solution(numbers) {
  // 오름차순 정렬
  let asc = numbers.sort((a, b) => a - b);
  // 큰 수 2개
  let maxnumbers = numbers.slice(-2);
  let answer = maxnumbers[0] * maxnumbers[1]
  return answer;
}

/**
 * function solution(numbers) {
    numbers.sort((a,b)=>b-a);
    return numbers[0]*numbers[1];
}

function solution(numbers) {
    let [a, b] = numbers.sort((a,b) => b - a);
    return a * b;
}
 */