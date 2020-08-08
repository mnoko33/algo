// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];
class Queue {
	constructor() {
		this.arr = [];
		this.maxSize = 10;
	}
	
	enqueue(v) {
		if (this.arr.length === this.maxSize) {
			console.log("overflow");
		} else {
			this.arr.push(v);
		}
	}
	
	dequeue() {
		if (!this.arr.length) {
			console.log("underflow")
		} else {
			this.arr.shift();
		}
	}
	
	printQ() {
		console.log(this.arr.join(' '));
	}
}

rl.on("line", function(line) {
	input.push(line);
}).on("close", function() {
	const Q = new Queue();
	let N = input[0];
	let idx = 1;
	while (N > 0) {
		const order = input[idx];
		if (order === 'd' || order ==='D') {
			Q.dequeue();
		} else if (order === 'e' || order === 'E') {
			idx += 1;
			const num = input[idx];
			Q.enqueue(num);
		} else {
			Q.printQ();
			return
		}
		N -= 1;
		idx += 1;
	}
	Q.printQ();
	process.exit();
});