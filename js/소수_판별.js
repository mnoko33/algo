function solution(N) {
    for (let i = 2; i <= parseInt(Math.sqrt(N)); i++) {
        if (N % i === 0) {
            return false;
        }
    }
    return true;
}


console.log(solution(2), true)
console.log(solution(3), true)
