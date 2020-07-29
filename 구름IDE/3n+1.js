// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

function solution(a, b) {
    let answer = 0;
    for (let i = a; i <= b; i ++) {
        answer = Math.max(answer, makeOne(i));
    }
    console.log(answer);

    function makeOne(n) {
        let cnt = 1;
        while (n > 1) {
            cnt += 1;
            if (n % 2 === 0) {
                n = n / 2;
            } else {
                n = 3 * n + 1;
            }
        }
        return cnt;
    }
}

rl.on("line", function(line) {
	const [a, b] = line.split(' ').map(x => Number(x))
	solution(a, b)
	rl.close();
}).on("close", function() {
	process.exit();
});