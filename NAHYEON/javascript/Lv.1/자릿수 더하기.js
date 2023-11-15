function solution(n)
{
    const digits = String(n).split('').map(Number);
    let answer = 0;
    for (let i = 0; i < digits.length; i++) {
        answer += digits[i];
    }
    return answer;
}