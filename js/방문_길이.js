function solution(dirs) {
    const D = new Map();
    D.set('U', [1,  0]);
    D.set('D', [-1, 0]);
    D.set('R', [0,  1]);
    D.set('L', [0, -1]);

    let answer = 0;
    let position = [0, 0];
    const history = [];
    for (let dir of dirs) {
        const [ud, lr] = D.get(dir);
        const [x, y] = position;
        const [nx, ny] = [x + ud, y + lr]
        // 경계체크
        if (nx > 5 || ny > 5 || nx < -5 || ny < -5) continue;

        position = [nx, ny]
        const route1 = `${x}${y}${nx}${ny}`;
        const route2 = `${nx}${ny}${x}${y}`;
        // 다녀온 길인지 체크
        if (!history.includes(route1) && !history.includes(route2)) {
            history.push(route1);
            history.push(route2);
            answer += 1;
        }
    }
    
    console.log(answer);
    return answer;
}

const dirs = "ULURRDLLU"
solution(dirs)

