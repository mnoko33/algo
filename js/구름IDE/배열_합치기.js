// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});
const input = []
function solution([sizeA, sizeB], A, B) {
    const arr = A.concat(B);
    arr.sort((a, b) => a - b);
    console.log(arr.join(' ') + ' ');
}

rl.on("line", function(a) {
	input.push(a.split(' ').map(x => Number(x)));
}).on("close", function() {
	solution(...input);
	process.exit();
});