function solution(s, n) {
  let answer = "";
  for (let i = 0; i < s.length; i++) {
    if (s[i] === " ") {
        answer += " ";
        continue;
    }
    else {
      let charCode = s.charCodeAt(i);
      // 대문자
      if (charCode <= 90) {
        charCode += n;
        // 변경 후 아스키코드값이 90보다 크다면
        if (charCode > 90) charCode -= 26;
      }
      // 소문자
      else {
        charCode += n;
        // 변경 후 아스키코드값이 122보다 크다면
        if (charCode > 122) charCode -= 26;
      }
      answer += String.fromCharCode(charCode);
    }
  }
  return answer;
}