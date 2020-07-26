function solution(user_id, banned_id) {
    const candidate = new Array(banned_id.length)
    for (let i = 0; i < candidate.length; i++) {
        candidate[i] = [];
        const bid = banned_id[i];
        for (let uid of user_id) {
            if (uid.length !== bid.length) continue;
            let flag = true;
            for (let k = 0; k < uid.length; k ++) {
                if (uid[k] !== '*' && bid[k] !== '*' && uid[k] !== bid[k]) {
                    flag = false;
                    break;
                }
            }
            if (flag) candidate[i].push(uid);
        }
    }

    let result = [];
    const N = candidate.length;
    let Q = [[0, []]];
    while (Q.length) {
        const [idx, arr] = Q.shift();
        if (idx === N) {
            result.push(arr);
            continue;
        }

        const ids = candidate[idx];
        for (let id of ids) {
            if (arr.includes(id)) continue;
            const newArr = arr.slice();
            newArr.push(id);
            Q.push([idx + 1, newArr]);
        }
    }

    result = result.map(arr => {
        return arr.sort();
    })
    
    const answer = [];
    for (let arr1 of result) {
        let isInclude = false;
        for (let arr2 of answer) {
            let isDiff = false;
            for (let i = 0; i < arr1.length; i++) {
                if (arr1[i] !== arr2[i]) {
                    isDiff = true;
                    break;
                }
            }
            if (!isDiff) {
                isInclude = true;
                break;
            }
        }
        if (!isInclude) answer.push(arr1);
    }
    return answer.length;
}


const user_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"];
const banned_id = ["*rodo", "*rodo", "******"]

solution(user_id, banned_id);