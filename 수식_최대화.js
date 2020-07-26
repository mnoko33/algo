function solution(expression) {
    let answer = 0;

    const orders = [
        ['+', '-', '*'],
        ['+', '*', '-'],
        ['-', '+', '*'],
        ['-', '*', '+'],
        ['*', '-', '+'],
        ['*', '+', '-'],
    ];

    let arr = exp2arr(expression);

    for (let order of orders) {
        let newArr = arr.slice();
        order.forEach(operator => {
            newArr = operate(newArr, operator);
        })
        answer = Math.max(answer, Math.abs(newArr[0]))
    }

    console.log(answer);
    return answer;

    function exp2arr(expression) {
        let result = [];
        let temp = '';
        for (let x of expression) {
            if (isNaN(x)) {
                result.push(Number(temp));
                temp = '';
                result.push(x);
            } else {
                temp += x;
            }
        }
        result.push(Number(temp))
        return result;
    }

    function calculate(n1, n2, operator) {
        if (operator === '+') return n1 + n2;
        if (operator === '-') return n1 - n2;
        if (operator === '*') return n1 * n2;
    }

    function operate(arr, operator) {
        const stack = [];
        for (let x of arr) {
            if (stack[stack.length - 1] === operator) {
                stack.pop();
                stack.push(calculate(stack.pop(), x, operator))
            } else {
                stack.push(x);
            }
        }
        return stack;
    }
}


const expression = "100-200*300-500+20"
solution(expression)