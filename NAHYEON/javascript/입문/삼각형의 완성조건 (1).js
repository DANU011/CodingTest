function solution(sides) {
  // 오름차순 정렬
  const asc = sides.sort((a, b) => a - b);
  // 배열의 마지막 값
  let last = asc[asc.length-1];
  let first = asc[0];
  let second = asc[1];
  if (last < first + second) return 1;
  else return 2;
}

/**
 * function solution(sides) {
    sides = sides.sort((a,b) => a-b)
    return sides[0]+sides[1] > sides[2] ? 1 : 2;
}

function solution(sides) {
    var answer = 0;
    const max = Math.max(...sides);
    const sum = sides.reduce((a,b) => a + b, 0) - max;

    answer = max < sum? 1 : 2;

    return answer;
}

function solution(sides) {
    const [long, a, b] = sides.sort((a,b) => b-a);

    return long < a + b ? 1 : 2


}
 */