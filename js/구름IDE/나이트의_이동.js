// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];
function solution(N, now, dest) {
		if (now[0] === dest[0] && now[1] === dest[1]) {
			console.log(0);
			return;
		}
    const Q = [[...now, 0]];
    const visited = new Array(N);
    for (let i = 0; i < N; i++) {
        visited[i] = new Array(N).fill(-1);
    }

    const DI = [-2, -1, 1, 2, 2, 1, -1, -2];
    const DJ = [1, 2, 2, 1, -1, -2, -2, -1];
    const D = 8;

    while (Q.length) {
        const [i, j, cnt] = Q.shift();
        for (let d = 0; d < D; d++) {
            const ni = i + DI[d];
            const nj = j + DJ[d];
            // 경계체크
            if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
            
            // 이미 방문 체크
            if (visited[ni][nj] === 1) continue;

            // 목적지 체크
            if (ni === dest[0] && nj === dest[1]) {
                console.log(cnt + 1);
                return;
            }

            visited[ni][nj] = 1;
            Q.push([ni, nj, cnt + 1]);
        }
    }
}

rl.on("line", function(line) {
	input.push(line.split(' ').map(x => Number(x)));
}).on("close", function() {
	const N = input[0][0];
	const now = input[1];
	const dest = input[2];
	solution(N, now, dest);
	process.exit();
});