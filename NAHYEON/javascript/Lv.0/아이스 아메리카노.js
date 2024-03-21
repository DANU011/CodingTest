function solution(money) {
    const americano = 5500;
    const coffee = Math.floor( money / americano );
    const change = money % americano;
    var answer = [coffee, change];
    return answer;
}