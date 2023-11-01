function solution(my_string) {
  let arr = [];
  for (let i = 0; i < my_string.length; i++) {
      // 대문자일 때
      if (my_string[i] == my_string[i].toUpperCase()) {
          arr.push(my_string[i].toLowerCase());
      }
      // 소문자일 때
      else {
          arr.push(my_string[i].toUpperCase());
      }
  }
  return arr.join(''); 
}