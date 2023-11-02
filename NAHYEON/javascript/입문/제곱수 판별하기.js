function solution(n) {
    var answer = Math.sqrt(n);
    var tf = Number.isInteger(answer);
    if (tf == true) return 1;
    else return 2;
}