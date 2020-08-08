function solution(numbers, hand) {
    var answer = '';
    var now_loc = [[3, 0], [3, 2]];
    const keypad = {
        1: [0, 0],
        2: [0, 1],
        3: [0, 2],
        4: [1, 0],
        5: [1, 1],
        6: [1, 2],
        7: [2, 0],
        8: [2, 1],
        9: [2, 2],
        0: [3, 1],
    };
    
    const leftSide = [1, 4, 7];
    const rightSide = [3, 6, 9];
    
    for (let i = 0; i < numbers.length; i++) {
        const num = numbers[i];
        const [x, y] = keypad[num];
        const left_dist = Math.abs(x - now_loc[0][0]) + Math.abs(y - now_loc[0][1]);
        const right_dist = Math.abs(x - now_loc[1][0]) + Math.abs(y - now_loc[1][1]);
        
        if (leftSide.find(x => x === num)) {
            answer = answer.concat('L');
            now_loc[0] = [x, y]
            continue;
        }

        if (rightSide.find(x => x === num)) {
            answer = answer.concat('R');
            now_loc[1] = [x, y]
            continue;
        }
        
        if (left_dist < right_dist || (left_dist === right_dist && hand === 'left')) {
            answer = answer.concat('L');
            now_loc[0] = [x, y]
        } else {
            answer = answer.concat('R');
            now_loc[1] = [x, y]
        }
    }
    return answer;
}


console.log(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right", "LRLLLRLLRRL"))