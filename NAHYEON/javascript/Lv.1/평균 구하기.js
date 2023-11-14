function solution(arr) {
  let total = 0;
  let count = 0;
  arr.forEach(function(item,index) {
      total += item;
      count++;
  });
  return total / count;
}