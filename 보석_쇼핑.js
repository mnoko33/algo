function solution(gems) {
    var answer = [1, gems.length];

    const gemsList = [...new Set(gems)];
    const GEMS_CNT = gemsList.length;
    const gemMap = new Map();

    let p1 = 0; // 포함시킬 idx pointer
    let p2 = 0; // 제외할 idx pointer

    while (p1 < gems.length && p2 < gems.length) {
        // p1번째 보석을 gemMap에 추가
        const gem = gems[p1];
        const temp = gemMap.get(gem);
        gemMap.set(gem, temp ? temp + 1 : 1);

        // 현재 보석을 모두 포함하고 있는 경우
        if (GEMS_CNT === gemMap.size) {
            while (p2 <= p1) {
                const targetGem = gems[p2];
                const targetGemCnt = gemMap.get(targetGem);
                if (targetGemCnt > 1) {
                    gemMap.set(targetGem, targetGemCnt - 1);
                } else {
                    gemMap.delete(targetGem);
                }
                // 만약 모든 보석을 포함하지 못한 경우가 발생한다면?
                if (GEMS_CNT !== gemMap.size) {
                    // console.log('...?')
                    if (p1 - p2 < answer[1] - answer[0]) {
                        answer = [p2 + 1, p1 + 1];
                    }
                    p2 += 1;
                    break;
                }
                p2 += 1;
            }
        }

        p1 += 1;
    }
    return answer;
}

console.log(solution(["DIA", "DIA", "DIA"]))