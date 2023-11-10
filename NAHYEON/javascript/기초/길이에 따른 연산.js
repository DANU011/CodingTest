function solution(num_list) {
  let add = 0;
  let mul = 1; 
  let answer = 0;
  if (num_list.length >= 11) {
      for (let i = 0; i < num_list.length; i++ ) {
          add = add + num_list[i];
          answer = add;
      }
  }
  else {
     for (let i = 0; i < num_list.length; i++ ) {
          mul = mul * num_list[i];
          answer = mul;
      } 
  }
  return answer;
}