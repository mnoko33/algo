// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];
function solution(N, arr, [s, e]) {
	let answer = 0;
	for (let i = s - 1; i <= e - 1; i++) {
		answer += arr[i];
	}
	console.log(answer);
}

rl.on("line", function(line) {
	input.push(line.split(' ').map(x => Number(x)))
}).on("close", function() {
	solution(...input);
	process.exit();
});