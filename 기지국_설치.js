function solution(n, stations, w) {
    let answer = 0;
    let start = 1;
    const N = stations.length;
    const rangePerStation = (1 + 2 * w);
    for (let i = 0; i < N; i++) {
        const station = stations[i];
        const end = station - w - 1;
        if (start <= end) {
            const sectionLength = end - start + 1;
            answer += Math.ceil(sectionLength / rangePerStation);
        }
        start = station + w + 1;
    }
    // 마지막 구간 추가
    if (start <= n) {
        const sectionLength = n - start + 1;
        answer += Math.ceil(sectionLength / rangePerStation);
    }

    return answer;
}

const n = 16
const stations = [9];
const w = 2;
console.log(solution(n, stations, w));