function solution(board) {
    const N = board.length;
    const DI = [1, 0, -1, 0];
    const DJ = [0, 1, 0, -1];
    const Q = [];
    const dist = new Array(N);
    for (let i = 0; i < N; i++) {
        dist[i] = new Array(N);
        for (let j = 0; j < N; j++) {
            dist[i][j] = -1;
        }
    }

    Q.push([0, 0, 0, 0], [0, 0, 0, 1]);
    dist[0][0] = 0;

    while (Q.length > 0) {
        const [i, j, c, d] = Q.shift();

        for (let k = 0; k < 4; k++) {
            const ni = i + DI[k];
            const nj = j + DJ[k];
            // 경계 체크
            if (ni < 0 || nj < 0 || ni >= N || nj >= N) continue;
            
            // 벽 체크
            if (board[ni][nj] === 1) continue;
            
            // 뒤로가기 체크
            if (Math.abs(d - k) === 2) continue;

            const cost = d === k ? 100 : 600;
            const target = dist[ni][nj];
            if (target === -1 || target >= c + cost) {
                dist[ni][nj] = c + cost;
                Q.push([ni, nj, c + cost, k])
            }
        }
    }

    return dist[N-1][N-1];
}


// const board = [[0,0,0],[0,0,0],[0,0,0]];
const board = [[0,0,0,0,0,0],[0,1,1,1,1,0],[0,0,1,0,0,0],[1,0,0,1,0,1],[0,1,0,0,0,1],[0,0,0,0,0,0]];
// const board = [[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0],[0,0,0,0,1,0,0,0],[0,0,0,1,0,0,0,1],[0,0,1,0,0,0,1,0],[0,1,0,0,0,1,0,0],[1,0,0,0,0,0,0,0]]
console.log(solution(board))