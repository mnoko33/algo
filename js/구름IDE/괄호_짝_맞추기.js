// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

rl.on("line", function(line) {
	const stack = [];
	let answer = 'True';
	for (let bracket of line) {
		if (bracket === '(' || bracket === '{' || bracket === '[') {
			stack.push(bracket);
			continue;
		}
		
		if (bracket === ')' && stack[stack.length - 1] === '(') {
			stack.pop();
			continue;
		}
		
		if (bracket === ']' && stack[stack.length - 1] === '[') {
			stack.pop();
			continue;
		}
		
		if (bracket === '}' && stack[stack.length - 1] === '{') {
			stack.pop();
			continue;
		}
		
		answer = 'False';
		break;
	}
	console.log(answer);
	
	rl.close();
}).on("close", function() {
	process.exit();
});