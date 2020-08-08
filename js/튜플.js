function solution(s) {
    const result = [];
    let subArray = [];
    let temp = '';
    for (let i = 0; i < s.length; i++) {
        const x = s[i];
        if (x === '{') continue;
        if (!isNaN(x)) temp += x;
        if ((x === ',' || x === '}') && temp !== '') {
            subArray.push(parseInt(temp));
            temp = '';
            if (x === '}') {
                result.push(subArray)
                subArray = [];
            }
        }
    }
    
    result.sort((a, b) => a.length - b.length)
    const answer = [];
    for (let arr of result) {
        for (let x of arr) {
            if (!answer.includes(x)) {
                answer.push(x)
            }
        }
    }
    return answer
}

s = "{{4,2,3},{3},{2,3,4,1},{2,3}}"
console.log(solution(s))