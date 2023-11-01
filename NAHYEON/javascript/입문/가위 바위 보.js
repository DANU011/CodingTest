function solution(rsp) {
  var answer = '';
  for (let i = 0; i < rsp.length; i++) {
      if (rsp[i] == "2") {
          answer += "0";
      }
      else if (rsp[i] == "0") {
          answer += "5";
      }
      else {
          answer += "2";
      }
  }
  return answer;
}

/**
 * 객체 사용법
 * function solution(rsp) {
    let arr = {
        2: 0,
        0: 5,
        5: 2
    };
    var answer = [...rsp].map(v => arr[v]).join("");
    return answer;
}

삼항연산자
function solution(rsp) {
    return rsp.split("").map((v) => v==="2" ? 0 : (v==="0" ? 5 : 2)).join("")
}
 */