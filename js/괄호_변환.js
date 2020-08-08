function solution(p) {
    return main(p);

    function main(p) {
        // 1단계
        if (p === '') return p;

        // 2단계
        const [u, v] = seperate(p);

        // 3단계
        if (isRight(u)) return u + main(v);

        // 4단계
        let temp = '(' + main(v) + ')';

        for (let i = 1; i < u.length - 1; i++) {
            if (u[i] === '(') {
                temp += ')';
            } else {
                temp += '(';
            }
        }
        return temp;
    }

    // p를 u와 v로 분리하는 함수
    function seperate(p) {
        const stack = [];
        let u = '';
        let v = '';
        let flag = false;
        for (let i = 0; i < p.length; i++) {
            const s = p[i];
            if (flag) {
                v += s;
            } else {
                u += s;
            }
            
            if (stack.length && stack[stack.length - 1] !== s) {
                stack.pop();
                if (!stack.length) flag = true;
            } else {
                stack.push(s);
            }
        }
        return [u, v];
    }

    function isRight(p) {
        const stack = [];
        for (let s of p) {
            if (s === '(') {
                stack.push(s);
            } else if (stack.length === 0) {
                return false;
            } else {
                stack.pop();
            }
        }
        return true;
    }
}


console.log(solution("()))((()"))