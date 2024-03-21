function solution(array) {
  var answer = 0;
  // 배열 길이 중 중앙값 찾기
  const mid = Math.floor( array.length/2 );
  // 오름차순 정렬
  const asc = array.sort((a, b) => a - b);
  answer = asc[mid];
  return answer;
}