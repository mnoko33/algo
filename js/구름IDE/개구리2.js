// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];

function solution(N, stones) {
    let hp = 0;
    let now;
    while (stones.length) {
        if (!now) {
            now = stones.pop();
            continue;
        }
        const before = stones.pop();
        hp = Math.max(now - before, hp + 1);
        now = before;
    }
    console.log(Math.max(now - 0, hp + 1));
}

rl.on("line", function(line) {
	input.push(line);
}).on("close", function() {
	const N = input[0];
	const stones = input[1].split(' ').map(x => Number(x))
	solution(N, stones);
	process.exit();
});