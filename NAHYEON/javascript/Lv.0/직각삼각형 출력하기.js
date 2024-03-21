const readline = require('readline');
const rl = readline.createInterface({
    input: process.stdin,
    output: process.stdout
});

let num;

rl.on('line', function (line) {
    num = Number(line); // 입력값을 숫자로 변환하여 num 변수에 저장
    rl.close(); // 입력 종료
}).on('close', function () {
    let logStr = '';
    for (let i = 0; i < num; i++) {
        for (let j = 0; j <= i; j++) {
            logStr += '*';
        }
        logStr += '\n';
    }
    console.log(logStr);
});
