function solution(n) {
  var arr = [];
  for (let i = 0; i <= n; i++) {
     if(i % 2 != 0) {
        arr.push(i); 
     }
  }
  return arr;
}