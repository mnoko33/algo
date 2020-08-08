// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];

function solution(N, routes) {
	let answer = -Infinity;
	const Q = [[0, 0, routes[0][0]]]; // i, j, acc
	while (Q.length) {
		let [i, j, acc] = Q.shift();

		k = routes[j].length;
		if (k === 1 && j > N) {
			answer = Math.max(answer, acc);
			continue;
		};
		j += 1;
		// 줄어들기
		if (j >= N) {
			if (i === 0 || i === k - 1) {
				const temp = i === 0 ? i : i - 1;
				Q.push([temp, j, acc + routes[j][temp]])
			} else {
				Q.push([i, j, acc + routes[j][i]]);
				Q.push([i - 1, j, acc + routes[j][i - 1]]);
			}
		// 늘어나기
		} else {
			Q.push([i, j, acc + routes[j][i]]);
			Q.push([i+1, j, acc + routes[j][i+1]]);
		}
	}
	console.log(answer);
}


rl.on("line", function(line) {
	input.push(line.split(' ').map(x => Number(x)));
}).on("close", function() {
	const N = input[0][0];
	const routes = input.slice(1, input.length);
	solution(N, routes);
	process.exit();
});