function solution(s) {
    let l = 0;
    let r = s.length - 1;
    let answer = '';
    while (l <= r) {
        if (l === r) {
            answer += s[l];
        } else {
            answer += s[l];
            answer += s[r];
        }
        l += 1;
        r -= 1;
    }
    
    return answer;
}


console.log(solution('abcdef'));
console.log(solution('Goorm'));