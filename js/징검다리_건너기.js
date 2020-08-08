function solution(stones, k) {
    let [minV, maxV] = [0, getMax(stones)];
    while (maxV - minV > 1) {
        const midV = parseInt((minV + maxV) / 2);
        if (isPossible(stones, k, midV)) {
            minV = midV;
        } else {
            maxV = midV - 1;
        }
    }

    return isPossible(stones, k, maxV) ? maxV : minV;

    function isPossible(stones, k, passed) {
        let cntZero = 0;
        for (let stone of stones) {
            if (stone - passed < 0) cntZero += 1;
            else cntZero = 0;

            if (cntZero >= k) return false;
        }
        return true;
    }

    function getMax(stones) {
        let maxV = -Infinity;
        for (let i = 0; i < stones.length; i++) {
            const stone = stones[i];
            maxV = Math.max(maxV, stone);
        }
        return maxV
    }
}


const stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1];
const k = 3;

console.log(solution(stones, k))