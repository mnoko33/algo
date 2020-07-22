function solution(progresses, speeds) {
    let answer = [];
    const N = progresses.length
    let left = [];
    for (let i = 0; i < N; i++) {
        const progress = progresses[i];
        const speed = speeds[i];
        const time = Math.ceil((100 - progress) / speed);
        if (left.length === 0 || left[0] >= time) {
            left.push(time)
        } else {
            answer.push(left.length);
            left = [time];
        }
    }
    if (left.length > 0) {
        answer.push(left.length);
    }

    return answer;
}


console.log(solution([93,30,55], [1,30,5]))