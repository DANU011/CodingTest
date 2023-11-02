function solution(before, after) {
  let beforeAsc = [...before].sort();
  let afterAsc = [...after].sort();
  
  return JSON.stringify(beforeAsc) === JSON.stringify(afterAsc)? 1 : 0;
}