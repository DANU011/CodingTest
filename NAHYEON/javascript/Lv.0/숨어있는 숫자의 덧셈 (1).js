function solution(my_string) {
  var answer = 0;
  // 정규표현식
  var regex = /[^0-9]/g;
  var result = my_string.replace(regex, "");
  let string = String(result);
  for (let i = 0; i < string.length; i++) {
      answer += parseInt(string[i]);
  }
  return answer;
}