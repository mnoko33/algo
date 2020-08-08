function solution(cookie) {
    const N = cookie.length;
    let answer = 0;
    const intervalSumArr = getIntervalSumArr(cookie);
    const TOTAL_CNT = intervalSumArr[N - 1];

    for (let l = 0; l < N; l++) {
        for (let m = l; m < N; m++) {
            const firstCnt = getIntervalSum(l, m);
            // 가지치기 조건
            if (firstCnt > TOTAL_CNT / 2) continue;
            if (firstCnt < answer) continue;

            for (let r = m + 1; r < N; r++) {
                const secondCnt = getIntervalSum(m + 1, r);
                if (firstCnt === secondCnt) {
                    if (firstCnt === TOTAL_CNT / 2) return firstCnt;
                    answer = Math.max(answer, firstCnt);
                }
            }
        }
    }

    return answer;

    function getIntervalSumArr(cookie) {
        const N = cookie.length;
        const arr = [];
        for (let i = 0; i < N; i++) {
            if (i === 0) {
                arr.push(cookie[i]);
            } else {
                arr.push(cookie[i] + arr[i - 1])
            }
        }
        return arr;
    }

    function getIntervalSum(s, e) {
        if (s === 0) {
            return intervalSumArr[e];
        }
        return intervalSumArr[e] - intervalSumArr[s - 1]; 
    }
}

let cookie = [1, 1, 2, 3];
console.log(solution(cookie))