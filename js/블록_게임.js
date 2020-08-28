// FAIL

function solution(board) {
  const N = board.length;
  // 오른쪽, 왼쪽, 아래 순으로 탐색
  const DR = [0,  0, 1];
  const DC = [1, -1, 0];
  const checked = new Array(N);
  for (let i = 0; i < N; i++) {
    checked[i] = new Array(N).fill(0);
  }

  let cnt = 0;

  for (let i = 0; i < N; i++) {
    for (let j = 0; j < N; j++) {
      // 블록 번호
      const block = board[i][j];
      // 방문할 필요가 없을 경우 패스
      if (checked[i][j]) continue;
      // 빈 곳인 경우 
      if (block === 0) continue;

      // i, j는 방문처리
      checked[i][j] = 1;
      const blockList = [[i, j]];
      const Q = [[i, j]];
      while (Q.length) {
        const [r, c] = Q.shift();
        for (let d = 0; d < 3; d++) {
          const nr = r + DR[d];
          const nc = c + DC[d];
          // 경계 확인
          if (nr < 0 || nc < 0 || nr >= N || nc >= N) continue;
          // 체크 확인
          if (checked[nr][nc]) continue;
          // 번호 확인
          if (board[nr][nc] !== block) continue;

          blockList.push([nr, nc])
          Q.push([nr, nc])
          checked[nr][nc] = 1;
        }
      }

      // blockList가 4개 미만일 경우 이미 위에서 막힌 경우
      if (blockList.length < 4) {
        blockList.forEach(([r, c]) => {
          while (r < N) {
            checked[r][c] = 1;
            r += 1;
          }
        })
        continue
      };

      // 해당 블록 리스트가 제거 가능한 것인지 확인
      /* 
          x    |     x
          x    |     x
          x x  |   x x
      */
      if (blockList[0][1] === blockList[1][1] && blockList[1][1] === blockList[2][1]) {
        const r1 = blockList[0][0];
        const r2 = blockList[1][0];
        const c = blockList[3][1];
        if (board[r1][c] === 0 && board[r2][c] === 0) {
          console.log(block);
          cnt += 1;
          continue;
        }
      } 

      /*  
            x     |   x       |       x
          x x x   |   x x x   |   x x x
      */
      if (blockList[1][0] === blockList[2][0] && blockList[2][0] === blockList[3][0]) {
        const r = blockList[0][0];
        const c1 = blockList[2][1];
        const c2 = blockList[3][1];
        if (board[r][c1] === 0 && board[r][c2] === 0) {
          blockList.forEach(([r, c]) => {
            board[r][c] = 0;
          })
          cnt += 1;
          continue;
        }
      }

      // 해당 블록의 아래에 있는 것들은 모두 checked = 1로 변경
      blockList.forEach(([r, c]) => {
        while (r < N) {
          blockList.forEach(([r, c]) => {
            board[r][c] = 0;
          })
          checked[r][c] = 1;
          r += 1;
        }
      })
    }
  }

  return cnt;
}

const board = [
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,0,0,0,0],
  [0,0,0,0,0,0,4,0,0,0],
  [0,0,0,0,0,4,4,0,0,0],
  [0,0,0,0,3,0,4,0,0,0],
  [0,0,0,2,3,0,0,0,5,5],
  [1,2,2,2,3,3,0,0,0,5],
  [1,1,1,0,0,0,0,0,0,5]
]
// const board = [
//   [0,0,0,0,0,0,0,0,0,0],
//   [0,0,0,0,0,0,0,0,0,0],
//   [0,0,0,0,0,0,0,0,0,0],
//   [0,0,0,0,0,0,0,0,0,0],
//   [0,0,0,0,0,0,0,0,0,0],
//   [0,0,0,0,0,0,0,0,0,0],
//   [0,0,0,0,0,0,1,0,0,0],
//   [0,0,0,2,2,2,1,0,0,0],
//   [0,0,0,2,0,1,1,0,0,0],
//   [0,0,0,0,0,0,0,0,0,0]
// ]
console.log(solution(board))