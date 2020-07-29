function solution(N, graph) {
    for (let k = 0; k < N; k++) {
        for (let i = 0; i < N; i++) {
            for (let j = 0; j < N; j++) {
                if (graph[i][k] === 0 || graph[k][j] === 0) continue;
                if (i === j) continue;
                if (graph[i][j] === 0 || graph[i][k] + graph[k][j] < graph[i][j]) {
                    graph[i][j] = graph[i][k] + graph[k][j];
                }
            }
        }
    }

    let answer = Infinity;
    for (let r = 0; r < N; r++) {
        const row = graph[r];
        let temp = 0;
        for (let x of row) {
            temp += x;
        }
        answer = Math.min(answer, temp);
    }
    console.log(answer);
}


const input = [ [ 10000 ], [ 0, 1, 2 ], [ 1, 2, 1 ], [ 1, 3, 7 ], [ 3, 4, 5 ] ]
const N = input[0][0];
const graph = new Array(N);
for (let i = 0; i < N; i++) {
    graph[i] = new Array(N).fill(0);
}
for (let [u, v, c] of input.slice(1, input.length)) {
    graph[u][v] = c;
    graph[v][u] = c;
}
solution(N, graph);