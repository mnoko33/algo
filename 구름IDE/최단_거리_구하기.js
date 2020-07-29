// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];

function solution(N, arr) {
	// dist 초기화
	const dist = new Array(N);
	for (let i = 0; i < N; i++) {
		dist[i] = new Array(N).fill(-1);
	}
	dist[0][0] = 1;
	
	// Direction 배열 생성
	dx = [0, 1, 0, -1];
	dy = [1, 0, -1, 0];
	
	Q = [[0, 0]];
	while (Q.length) {
		const [x, y] = Q.shift();
		for (let i = 0; i < 4; i++) {
			const nx = x + dx[i];
			const ny = y + dy[i];
			// 경계체크
			if (nx < 0 || ny < 0 || nx >= N || ny >= N) continue;
			// 방문 가능 체크
			if (arr[nx][ny] === 0) continue;
			// 최소비용 체크
			if (dist[nx][ny] === -1 || dist[nx][ny] > dist[x][y] + 1) {
				dist[nx][ny] = dist[x][y] + 1;
				Q.push([nx, ny])
			}
		}
	}

	if (dist[N-1][N-1] > 0) {
		console.log(dist[N-1][N-1])
	}
}

rl.on("line", function(line) {
	input.push(line.split(' ').map(x => Number(x)));
}).on("close", function() {
	const N = input[0][0];
	const arr = input.slice(1, input.length);

	solution(N, arr);
	process.exit();
});