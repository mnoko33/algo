// Run by Node.js

const readline = require("readline");
const rl = readline.createInterface({
	input: process.stdin,
	output: process.stdout
});

const input = [];

function solution(N, boxList) {
    boxList.sort((a, b) => {
        return Math.abs(b) - Math.abs(a);
    })

    const container = [-1, 1]   // [black, white];
    const cnt = [0, 0]          // [black, white];
    for (let i = 0; i < N; i++) {
        const box = boxList[i];
        if (box > 0) {
            // black 우선
            if (container[0] === -1) {
                cnt[0] += 1;
                container[0] = 1;
            }
            // white 우선
            if (container[1] === -1) {
                cnt[1] += 1;
                container[1] = 1;
            }
        } else {
            // black 우선
            if (container[0] === 1) {
                cnt[0] += 1;
                container[0] = -1;
            }
            // white 우선
            if (container[1] === 1) {
                cnt[1] += 1;
                container[1] = -1;
            }
        }
    }
    console.log(Math.max(...cnt));
}

rl.on("line", function(line) {
	input.push(Number(line))
}).on("close", function() {
	const [N, ...boxList] = input;
	solution(N, boxList);
	process.exit();
});