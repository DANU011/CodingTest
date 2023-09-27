function solution(hp) {
  // 장군개미 수
  let a5 = parseInt(hp / 5);
  // 병정개미 수
  let a3 = parseInt ((hp % 5) / 3);
  // 일개미 수
  let a1 = hp - (5 * a5 + 3 * a3);
  let answer = a5 + a3 + a1;
  return answer;
}

/**
 * function solution(hp) {
    return Math.floor(hp/5)+Math.floor((hp%5)/3)+(hp%5)%3;
}

function solution(hp) {
    const 장군개미 = Math.floor(hp / 5);
    const 병정개미 = Math.floor((hp - (장군개미 * 5)) / 3);
    const 일개미 = hp - ((장군개미 * 5) + (병정개미 * 3));
    return 장군개미+병정개미+일개미;
}
 */