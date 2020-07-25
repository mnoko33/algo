function solution(lines) {
    lines = lines.map(line => {
        line = line.split(' ');
        const S = line.slice(0, line.length - 1).join(' ');
        const T = line[line.length - 1];
        const date = new Date(S)
        const EndWithSeconds = date.getHours() * 3600 + date.getMinutes() * 60 + date.getSeconds() + date.getMilliseconds() / 1000;
        const startWithSeconds = EndWithSeconds - Number(T.substring(0, T.length - 1)) + 0.001;
        return [startWithSeconds, EndWithSeconds]
    })

    let answer = 0;
    for (let i = 0; i < lines.length; i++) {
        let tempAns = 1;
        const [s1, e1] = lines[i];
        for (let j = i + 1; j < lines.length; j++) {
            const [s2, e2] = lines[j];
            if (s2 < e1 + 1) tempAns += 1;
        }
        answer = Math.max(answer, tempAns);
    }
    return answer;
}


lines = ["2016-09-15 20:59:57.421 0.351s", "2016-09-15 20:59:58.233 1.181s", "2016-09-15 20:59:58.299 0.8s", "2016-09-15 20:59:58.688 1.041s", "2016-09-15 20:59:59.591 1.412s", "2016-09-15 21:00:00.464 1.466s", "2016-09-15 21:00:00.741 1.581s", "2016-09-15 21:00:00.748 2.31s", "2016-09-15 21:00:00.966 0.381s", "2016-09-15 21:00:02.066 2.62s"]

console.log(solution(lines))