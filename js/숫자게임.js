function solution(A, B) {
    let answer = 0;
    
    A.sort((x, y) => y - x);
    B.sort((x, y) => y - x);
    let ai = 0, bi = 0;
    const N = A.length
    while (ai < N && bi < N) {
        if (A[ai] < B[bi]) {
            answer += 1;
            ai += 1;
            bi += 1;
        } else {
            ai += 1;
        }
    }
    return answer;
}

const A = [2, 3, 4, 5, 6, 7]
const B = [3, 4, 5, 6, 7, 2]
console.log(solution(A, B));